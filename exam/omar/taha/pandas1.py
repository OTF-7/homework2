import pandas as pd


def pandas_test():
    sentence = 'The quick brown fox jumps over a lazy dog.'
    words = sentence.split(' ')
    df1 = pd.DataFrame({'key': range(len(words)),
                        'column1_Words': words,
                        'column2_Length': [len(x) for x in words]})
    print(df1)
