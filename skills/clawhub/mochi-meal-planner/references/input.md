# Input contract

plan: meals [{date,slot breakfast|lunch|dinner,dish,servings,ingredients:[{name,quantity,unit}]}], optional exclude [ingredient names], pantry [{name,quantity,unit}], budget {amount,currency}. Quantities cover the meal’s total servings. g/kg and ml/l are normalized; different unconvertible units remain separate. show: id. Plan writes require requestId.

Currency fields support CNY, USD, EUR, GBP, HKD, SGD, AUD, CAD, CHF and NZD with two decimal places. The sample is fictional. Copy it into an authorized workspace and replace its facts and dates before real use. Current-agent state is stored separately for each workspace. A duplicate requestId with identical input returns the prior result; reusing it with changed data returns an error. A busy lock means another operation is active: wait rather than removing its lock.
