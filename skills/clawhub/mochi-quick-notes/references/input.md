# Input contract

add: kind note|task|idea, text, optional tags (max 3), due YYYY-MM-DD. list/search: optional status, kind; search requires query and performs literal normalized substring matching. complete/archive: id. Mutations require requestId. Archived records are retained and can be listed with status archived.

Currency fields support CNY, USD, EUR, GBP, HKD, SGD, AUD, CAD, CHF and NZD with two decimal places. The sample is fictional. Copy it into an authorized workspace and replace its facts and dates before real use. Current-agent state is stored separately for each workspace. A duplicate requestId with identical input returns the prior result; reusing it with changed data returns an error. A busy lock means another operation is active: wait rather than removing its lock.
