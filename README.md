# ColonCancer_survival

1. Use command conda create --name env_name --file requirements.txt to create the appropitate conda environment

2. Activate env as: conda activate env_name

3. Run the test as: 
python main.py --testdata test_file.csv --flag Test

4. This code reads the histopathology image features in a CSV file as

Study ID	CENTER, 1-UPMC, 2=Mt. Sinai, 3=ACCESS, 11=Ontario, 13=Australia, 14=Hawaii, 15=Mayo, 16=Seattle	Stage	Recurrence status at last F/up, 0=No recurrence, 1=recurrence	Time to recurrence or last follow-up (months)	MMR status, 0=MMRP, 0=MMRD	%Tumor within tumor bed	%Stroma within tumor bed	%Mucin within tumor	%necrosis within tumor bed	%TB/PDC within tumor	Tumor:Stroma Ratio	TILs per mm2 tumor	%High-grade	%SRCC	%Immature within tumor bed	%inflammatory within tumor bed	%mature within tumor bed	%immature within stromal region	%inflammatory within stromal region	%mature within stromal region


5. Saves the output in ./output/Test_prediction.csv


Please refer to: Pai, Reetesh K., Imon Banerjee, Sameer Shivji, Suchit Jain, Douglas Hartman, Daniel D. Buchanan, Mark A. Jenkins et al. "Quantitative Pathologic Analysis of Digitized Images of Colorectal Carcinoma Improves Prediction of Recurrence-Free Survival." Gastroenterology 163, no. 6 (2022): 1531-1546.






