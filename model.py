import pandas as pd


def load_processed_data(file_name):
    """
    Returns processed dataset along with X matrix and y vector

    :param file_name: enter absolute path of the .csv datafile
    :return: dataset, X, y
    """

    # Load dataset
    df = pd.read_csv(filepath_or_buffer=file_name)

    # Fill NaN values
    df['experience'].fillna(value=0, inplace=True)
    df['test_score'].fillna(value=df['test_score'].mean(), inplace=True)

    # Declare X and y values
    X_ = df.iloc[:, :-1]
    y_ = df.iloc[:, -1]

    # Pre-processing
    word_dict = {'one': 1, 'two': 2, 'three': 3,
                 'four': 4, 'five': 5, 'six': 6,
                 'seven': 7, 'eight': 8, 'nine': 9,
                 'ten': 10, 'eleven': 11, 'twelve': 12,
                 'zero': 0, 0: 0}
    X_['experience'] = X_['experience'].apply(lambda i: word_dict[i])

    return df, X_, y_


if __name__ == '__main__':
    import pickle
    from sklearn.linear_model import LinearRegression
    filename = '/home/nm/PycharmProjects/pythonProject/data/hiring.csv'
    dataset, X, y = load_processed_data(file_name=filename)

    regressor = LinearRegression()
    regressor.fit(X, y)
    pickle.dump(regressor, open('model.pkl', 'wb'))

    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    print(model.predict([[2, 9, 6]]))
