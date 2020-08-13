linreg = LinearRegression()
linreg_r2 = fit_and_eval(linreg)

random_forest = RandomForestRegressor(random_state=19)
random_forest_r2 = fit_and_eval(random_forest)

extra_trees = ExtraTreesRegressor(random_state=19)
extra_trees_r2 = fit_and_eval(extra_trees)

grad_boost = GradientBoostingRegressor(random_state=19)
grad_boost_r2 = fit_and_eval(grad_boost)

lasso = Lasso(random_state=19)
lasso_r2 = fit_and_eval(lasso)

ridge = Ridge(random_state=19)
ridge_r2 = fit_and_eval(ridge)

svr = SVR()
svr_r2 = fit_and_eval(svr)

knn = KNeighborsRegressor()
knn_r2 = fit_and_eval(knn)