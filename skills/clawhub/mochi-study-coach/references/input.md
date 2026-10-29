# Input contract

add: topic, question, answer, source, date. due: date, optional topic; answer and review history are omitted from due output. show: id. grade: id, date, grade 0..3, response, feedback. A low grade resets the interval; successful reviews extend it. Mutations require requestId.

Currency fields support CNY, USD, EUR, GBP, HKD, SGD, AUD, CAD, CHF and NZD with two decimal places. The sample is fictional. Copy it into an authorized workspace and replace its facts and dates before real use. Current-agent state is stored separately for each workspace. A duplicate requestId with identical input returns the prior result; reusing it with changed data returns an error. A busy lock means another operation is active: wait rather than removing its lock.
