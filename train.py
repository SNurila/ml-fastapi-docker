{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "889859d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import numpy as np\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "import joblib\n",
    "df = pd.read_csv('/Users/nurilasalamat/Documents/ml/practice6/tesla_stock_data_2010_2025.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a842d5fe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['model.joblib']"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = df.dropna()\n",
    "\n",
    "# select features \n",
    "features = [\n",
    "    \"Open\", \"High\", \"Low\", \"Volume\",\n",
    "    \"Daily_Return\", \"Price_Range\",\n",
    "    \"Price_Change\", \"Price_Change_Percent\",\n",
    "    \"MA_7\", \"MA_30\", \"MA_90\",\n",
    "    \"Volatility_7d\"\n",
    "]\n",
    "\n",
    "X = df[features]\n",
    "y = df[\"Close\"]\n",
    "\n",
    "# split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)\n",
    "\n",
    "# model\n",
    "model = RandomForestRegressor()\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "joblib.dump(model, \"model.joblib\")\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv (3.11.14)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
