# Input contract

add: kind expense|income|refund, date, amount (decimal string, max 2 places), currency (3 uppercase letters), category, optional description. void: id, reason. budget: month YYYY-MM, amount, currency, category. list/summary: from and to inclusive dates. Amounts in outputs are minor units (100 = 1 major unit). Mutations require requestId.

Currency fields support CNY, USD, EUR, GBP, HKD, SGD, AUD, CAD, CHF and NZD with two decimal places. The sample is fictional. Copy it into an authorized workspace and replace its facts and dates before real use. Current-agent state is stored separately for each workspace. A duplicate requestId with identical input returns the prior result; reusing it with changed data returns an error. A busy lock means another operation is active: wait rather than removing its lock.
