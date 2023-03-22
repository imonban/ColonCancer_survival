import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from lifelines.utils import concordance_index
from lifelines import KaplanMeierFitter
import scipy.stats as st
import random
from lifelines import CoxPHFitter
import sys





class Survial_Model(object):
    def __init__(self):
        self.cox_model = None
        self.train = None
        self.test = None
    def convert_3months(self, T):
        return int(T/2)*2
    def encode(self, train):
        ## Time to event till 4 years - 48 months
        T = []
        E = []

        for i in range(train.shape[0]):
            if train.iloc[i]['Time to recurrence or last follow-up (months)'] < 60: # 5 years
                T.append(self.convert_3months(train.iloc[i]['Time to recurrence or last follow-up (months)']))
                E.append(train.iloc[i]['Recurrence status at last F/up, 0=No recurrence, 1=recurrence'])
            else:
                T.append(60)
                E.append(0)
        train['Event'] = E
        train['Time to event'] = T
        train = train.drop(['Time to recurrence or last follow-up (months)', 'Recurrence status at last F/up, 0=No recurrence, 1=recurrence'], axis=1)
        return train

    def grid_cox(df_stage_train, df_stage_test_1):
        al = np.arange(0.05, 0.99, 0.05)
        l1 = np.arange(0.05, 0.99, 0.1)
        results = {}
        for i  in al:
            for l in l1:
                cph =  CoxPHFitter(alpha = i, l1_ratio = l)
                cph.fit(df_stage_train, 'Time to event', event_col='Event', step_size=1) 
                Cindex_internal = concordance_index(df_stage_test_1['Time to event'], -cph.predict_partial_hazard(df_stage_test_1), df_stage_test_1['Event'])
                results[str(i)+'_'+str(l)] = Cindex_internal
        return results

    def train_main(self, traindf, testdf):
    ##load pretarined model 
        self.train = self.encode(traindf)
        self.test = self.encode(testdf)
        #self.train = traindf
        #self.test = testdf
        df_stage_train = self.train[['Stage','MMR status, 0=MMRP, 0=MMRD','%Tumor within tumor bed','%Stroma within tumor bed',
                                '%Mucin within tumor','%necrosis within tumor bed','%TB/PDC within tumor','Tumor:Stroma Ratio',
                                'TILs per mm2 tumor','%High-grade','%SRCC','%Immature within tumor bed','%inflammatory within tumor bed',
                                '%mature within tumor bed','%immature within stromal region','%inflammatory within stromal region','%mature within stromal region',
                                'Time to event', 'Event']]
        df_stage_test = self.test[['Stage','MMR status, 0=MMRP, 0=MMRD','%Tumor within tumor bed','%Stroma within tumor bed',
                                '%Mucin within tumor','%necrosis within tumor bed','%TB/PDC within tumor','Tumor:Stroma Ratio',
                                'TILs per mm2 tumor','%High-grade','%SRCC','%Immature within tumor bed','%inflammatory within tumor bed',
                                '%mature within tumor bed','%immature within stromal region','%inflammatory within stromal region','%mature within stromal region',
                                'Time to event', 'Event']]

        self.cox_model =  CoxPHFitter(alpha = 0.1, l1_ratio = 0.5)
        self.cox_model.fit(df_stage_train, 'Time to event', event_col='Event', step_size=1)
        self.cox_model.print_summary()
        
    def model_load(self, modelpath):
        try:
            self.cox_model = pickle.load(open(modelpath+'CoxModel.sav', 'rb'))
            print('Model loaded!!')
        except:
            sys.exit('Model couldn\'t be loaded')

    def model_save(self, modelpath):
        try:
            pickle.dump(self.cox_model, open(modelpath+'CoxModel.sav', 'wb'))
            print('Model saved!!')
        except:
            print('Model saving didn\'t worked')

    def test_main(self, testdf):
        #try:
            self.test = self.encode(testdf)
            #self.test = testdf
            
            df_stage_test = self.test[['Stage','MMR status, 0=MMRP, 0=MMRD','%Tumor within tumor bed','%Stroma within tumor bed',
                                '%Mucin within tumor','%necrosis within tumor bed','%TB/PDC within tumor','Tumor:Stroma Ratio',
                                'TILs per mm2 tumor','%High-grade','%SRCC','%Immature within tumor bed','%inflammatory within tumor bed',
                                '%mature within tumor bed','%immature within stromal region','%inflammatory within stromal region','%mature within stromal region',
                                'Time to event', 'Event']] ##full model
            
            '''
            df_stage_test = self.test[['Stage','MMR status, 0=MMRP, 0=MMRD',
                                'Time to event', 'Event']] ##stage and MMR
            '''
            Prediction_test = self.cox_model.predict_survival_function(df_stage_test)
            df_stage_test['Hazards']  = -self.cox_model.predict_partial_hazard(df_stage_test)
            for i in range(Prediction_test.shape[0]):
                df_stage_test[str(i*2)+'months'] = Prediction_test.iloc[i,:]
            df_stage_test['Study ID']  = self.test['Study ID']
            
        #except:
        #    sys.exit('Please provide a correct test file and model path with Comments')
            return df_stage_test


