# The Kronforst Scale Project: A Scale Morphology Analysis Program - Architecture 
```
 Resource_Manager
  ├── ARCHITECTURE.md    # This File.
  ├── .gitignore         # Git Ignore File.        
  ├── README.md          # Project Description.
  ├── src                # All source code in this repo.
  | ├── color.py         # Applies color classification methods to re-label the 'scale_color' variable in our data . 
  │ ├── main.py          # Runs our program, mutant analysis or family analysis. WARNING: >> ipython3 main.py will spam your browser.
  | ├── phy_tree.py      # Contains Tree() Object which creates a phylogenetic tree of input data. 
  | ├── scale_data.py    # Creates Pandas DataFrame from our Google Spreadsheets database.
  | ├── viz_data.py      # Has different functions to visualize the data, reduce the dimensionality of it, and select. 
  ├── img                # Contains images referenced to in ReadMe file.
  | ├── phy_tree         # Images of Phylogenetic Trees referenced to in ReadMe file.
  | ├── all_PCA          # Images of PCA's referenced to in ReadMe file.
  | ├── dark_vs_light    # Images of PCA's of dark vs. light scale classification referenced to in ReadMe file.
  | ├── family_analysis  # Images of PCA's by family referenced to in ReadMe file.
  | ├── mutants          # Images of PCA's by pre-mutant to post-mutant scales referenced to in ReadMe file.
  ├── data               # Sample of data used to generate some of the images. (full data available after publication)
  | ├── secret.json        # NOT INCLUDED - contains link to our database (will be pushed once published).
```
