# Input contract

compare: asOf YYYY-MM-DD, criteria [], items [{name,url,observedOn,currency,evidence, optional price,shipping,discount,quantity,specs}]. Decimal strings have up to two places. Shipping omitted means unknown, not free. Costs rank separately by currency; each result includes quantity and unitTotalMinor. show: id. Compare requires requestId.

Currency fields support CNY, USD, EUR, GBP, HKD, SGD, AUD, CAD, CHF and NZD with two decimal places. The sample is fictional. Copy it into an authorized workspace and replace its facts and dates before real use. Current-agent state is stored separately for each workspace. A duplicate requestId with identical input returns the prior result; reusing it with changed data returns an error. A busy lock means another operation is active: wait rather than removing its lock.
