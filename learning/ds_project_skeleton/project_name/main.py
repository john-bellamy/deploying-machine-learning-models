

#imports

x_train, y_train, x_test, y_test = get_data()
model = MyModel()
model.fit(x_train, y_train)
model.score(x_test, y_test)
