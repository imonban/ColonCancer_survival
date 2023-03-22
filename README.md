# ColonCancer_survival

Use command conda create --name <env> --file requirements.txt to create the appropitate conda environment

Activate env as: conda activate <env>

Run the test as: 
python main.py --testdata test_file.csv --flag Test

This code reads the histopathology image features in a CSV file as

Study ID	CENTER, 1-UPMC, 2=Mt. Sinai, 3=ACCESS, 11=Ontario, 13=Australia, 14=Hawaii, 15=Mayo, 16=Seattle	Stage	Recurrence status at last F/up, 0=No recurrence, 1=recurrence	Time to recurrence or last follow-up (months)	MMR status, 0=MMRP, 0=MMRD	%Tumor within tumor bed	%Stroma within tumor bed	%Mucin within tumor	%necrosis within tumor bed	%TB/PDC within tumor	Tumor:Stroma Ratio	TILs per mm2 tumor	%High-grade	%SRCC	%Immature within tumor bed	%inflammatory within tumor bed	%mature within tumor bed	%immature within stromal region	%inflammatory within stromal region	%mature within stromal region


Saves the output in ./output/Test_prediction.csv






