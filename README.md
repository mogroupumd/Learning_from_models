# Learning_from_models
&emsp; The performance datasets and the analysis notebooks for the publication "Learning from models: high-dimensional analyses on the performance of machine learning interatomic potentials"  
  
# Data
&emsp; The performance datasets  $\mathcal{D}_ {\mathrm{2300}}$  and $\mathcal{D}_ {\mathrm{124}}$ are in the directory `data/`. `D124_log.csv` corresponds to the $\mathcal{D}_ {\mathrm{124}}$, but all error metrics are log errors ($\mathrm{log}_ {\mathrm{10}}$ $\delta$) and the benchmark row is labelled as **DFT** (row 126, or index 125). The $\mathcal{D}_ {\mathrm{2300}}^ {\mathrm{48}D}$ can simply be reproduced by removing properties in the energy ranking category in $\mathcal{D}_{\mathrm{2300}}$, so we don't have a separate file for it. Data to reproduce the figures in different sections are in the directory `data/`. Detailed locations of data for these figures can be found in the analysis notebooks.  
**Note**: the `N-optimal_random_variables.png` in `data/` is a figure mentioned in Notebook 04, which corresponds to an analysis not included in the publication.  
  
# Notebooks
Each notebook corresponds to an analysis in the paper:  
  
 - <u>Notebook 01</u>: Figure 4, section 2.3  
 - <u>Notebook 02</u>: Figure 5, Supplementary Figure S5 and S6, section 2.4  
 - <u>Notebook 03</u>: Figure 7, Supplementary Figure S8, S9, S10, and S11, section 2.6  
 - <u>Notebook 04</u>: <u>*Related to*</u> Supplementary Figure S7  
  
# Other algorithms and methods
&emsp; Several algorithms and methods are from online, including the algorithms to compute Pareto fronts, inverted generational distance, and the Cholesky method. Their websites are in corresponding files and notebooks. References about other packages or algorithms are in the Methods of the paper.  
  
# Citation
If you use the datasets or the analyses extensively, you may want to cite the following publication:  
Y. Liu, Y. Mo, Learning from models: high-dimensional analyses on the performance of machine learning interatomic potentials. (ready to submit)  
