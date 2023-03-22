import pandas as pd
import os
import argparse
import sys
import train

# Instantiate the parser
parser = argparse.ArgumentParser()
parser.add_argument('--modelpath', type=str,
                    default="./model/", 
                    help='path to the trained model')
parser.add_argument('--traindata', type=str, default="./Data/DataCodebase/train.csv",
                    help='path to the train .csv file that contains comments with labels ')
parser.add_argument('--validationdata', type=str, default="./Data/DataCodebase/internal_test.csv", 
                    help='path to the validation file .csv that contains comments with labels; only needed for training')
parser.add_argument('--testdata', type=str, default="./Data/DataCodebase/external_test.csv", 
                    help='path to the test file .csv that contains comments without labels; only needed for testing ')
parser.add_argument('--savepath', type=str, default="./output/Test_prediction.csv", 
                    help='path to save the annotated test file .csv that contains model derieved prediction; only needed for testing')
parser.add_argument('--flag', type=str, default='Test', 
                    help='flag to signify the mode of model use -  Train/Test')



# parse the arguments
args = parser.parse_args()


def main():
    surCox = train.Survial_Model()
    if args.flag == 'Train':
        try:
            traindf = pd.read_csv(args.traindata)
            validdf = pd.read_csv(args.validationdata)
            surCox.train_main(traindf, validdf)
            surCox.model_save(args.modelpath)
        except:
            sys.exit('Enter the path for the correct .csv file or model saving path')
    if args.flag == 'Test':
        try:
            testdf = pd.read_csv(args.testdata)
            surCox.model_load(args.modelpath)
            annotated_test = surCox.test_main(testdf)
            print('finished the COX prediction')
            annotated_test.to_csv(args.savepath)
            print('Saved the data to: '+args.savepath)
        except:
            sys.exit('Enter the path for the correct .xlsx file or model saving path')
      
    


if __name__ == "__main__":
    main()