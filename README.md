# streamlit-aggrid


<br>

# Install
```
pip install streamlit-aggrid

```

# Quick Use
Create an example.py file
```python
from st_aggrid import AgGrid
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
AgGrid(df)
```
Run :
```shell
streamlit run example.py
```
