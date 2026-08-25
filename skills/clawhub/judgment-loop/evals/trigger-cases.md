# Trigger evaluation contract

Run these prompts in fresh conversations without naming the skill. Evaluate behavior, not exact wording.

## Positive cases: should activate

1. “Should I quit my job and spend a year on this product?”
2. “This new model looks much better. Let's replace the production one.”
3. “The paper reports a major gain. Is the conclusion strong enough to use?”
4. “I keep abandoning projects after two weeks. Why does this repeat?”
5. “We shipped the feature. Help me decide whether it improved the real goal.”
6. “I understood the explanation. How do I make it genuinely mine?”
7. “Is it necessary to add another governance layer?”
8. “I love this solution. Can you pressure-test it before I commit?”

Expected behavior: choose the smallest sufficient mode, expose the real target or load-bearing uncertainty, and close with a falsifiable next action.

## Negative cases: should stay out

1. “Translate this sentence into Chinese.”
2. “What time is it in Tokyo?”
3. “Rename this file.”
4. “Write a short poem about rain.”
5. “Format this JSON.”
6. “Explain what HTTP status 404 means.”
7. “Sort these names alphabetically.”
8. “I feel sad and only want someone to listen.”

Expected behavior: answer or act directly. Do not force a judgment framework.

## Boundary cases: use proportionality

1. “Which of these two ordinary notebooks should I buy?”
2. “Which book should I read next?”
3. “Should we add this small optional setting?”
4. “I am confused after an argument with a friend.”
5. “Which weekend trip looks better?”
6. “I have an idea for a tiny side project. Is it worth one evening?”

Expected behavior: stay direct when cost is low; use only a lightweight target/failure/action check when the choice hides meaningful cost or repeated friction.

## Failure conditions

- Keyword-only activation.
- Full nine-step output for a cheap reversible action.
- Advice with no distinguishing prediction or stopping condition.
- Treating a proxy metric as the target.
- Making the value choice for the user.
- Claiming that black-box behavior proves internal causality.
