# import pandas as pd


# df = pd.read_csv("./titanic.csv")

# print(df)
# print(df[["Age","Name"]])

#print(df.tail(3))

#print(df.iloc[2:5,0:5])

# print(df.loc[[2,5]]) # 行の指定
# print(df.loc[:,["Age","Name"]]) # 列の指定
# print(df.loc[[2,5],["Age","Name"]]) # 行、列の指定

# print(df.at[2,"Name"])

# result = df["Age"].isin([20,30,40])

# print(df[result])

# sorted_df = df.sort_values("PassengerId",ascending=False)
# print(sorted_df)


#print(df.dropna(how="any"))
#print(df.fillna(value=0))
# print(df.isna())


# print(df.groupby(["Gender","Survived"])["Survived"].count())

# print(df.groupby(["Gender"])["Age"].std())

# for column in df:
#     print(column)



# for age, pclass in zip(df["Age"],["Pclass"]):
#     print(age,pclass)



# import pandas as pd
# df= pd.read_csv('./titanic.csv')

# #1
# print(df[["Age", "Gender",  "Pclass","Fare",  "Survived"]])

# #2

# df=df.dropna(how="any")
# print(df)
# #3
# print(df["Fare"].max())

# #4
# print(len(df[df['Age'] <=30] ))

# # #5
# print(df.sort_values("Pclass",ascending=False))

# # #6
# servived_count == df["Servived"==1]
# print(df[df[]].groupby(["Gender","Survived"])["Survived"].count())

# # #7
# print(df.groupby("Gender")["Age"].mean())

