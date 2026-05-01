from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

app = Flask(__name__)
CORS(app)

@app.route('/rules', methods=['GET'])
def get_rules():
    data = [
        ['Milk', 'Bread', 'Butter'],
        ['Beer', 'Diaper', 'Milk'],
        ['Milk', 'Bread', 'Diaper', 'Beer'],
        ['Bread', 'Butter'],
        ['Milk', 'Diaper', 'Beer', 'Cola']
    ]

    te = TransactionEncoder()
    te_array = te.fit(data).transform(data)
    df = pd.DataFrame(te_array, columns=te.columns_)

    frequent_items = apriori(df, min_support=0.4, use_colnames=True)
    rules = association_rules(frequent_items, metric="confidence", min_threshold=0.6)

    def convert(item):
        return ', '.join(list(item))

    rules['antecedents'] = rules['antecedents'].apply(convert)
    rules['consequents'] = rules['consequents'].apply(convert)

    result = rules[['antecedents','consequents','support','confidence','lift']].round(2)

    return jsonify(result.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)

