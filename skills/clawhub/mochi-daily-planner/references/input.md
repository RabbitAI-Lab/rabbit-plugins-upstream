# Input contract

plan: date, availableMinutes 1..1440, tasks [{title,minutes 1..1440,priority 1..3}]. show: date. complete: date, taskId. rollover: from, to (later date), availableMinutes if target day is new. Rollover marks original open tasks deferred and copies them once. Mutations require requestId.

Currency fields support CNY, USD, EUR, GBP, HKD, SGD, AUD, CAD, CHF and NZD with two decimal places. The sample is fictional. Copy it into an authorized workspace and replace its facts and dates before real use. Current-agent state is stored separately for each workspace. A duplicate requestId with identical input returns the prior result; reusing it with changed data returns an error. A busy lock means another operation is active: wait rather than removing its lock.
