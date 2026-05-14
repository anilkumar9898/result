#%%
import pandas as pd
dic={
    "hours":[3,4,5,6,7,8,9],
    "marks":[35,45,55,65,75,85,95]

}
df=pd.DataFrame(dic)
# print(df)
# %%
x=df[["hours"]]
y=df["marks"]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)
print(model.predict([[7]])[0])

# %%
# in order to store the model , we use pickle library
import pickle
with open("linear_model.pkl","wb") as f:
    pickle.dump(model,f)
# %%
