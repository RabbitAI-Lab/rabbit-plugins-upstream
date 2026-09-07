# IA validation and measurement

Read this reference when proposing tests, evaluating an IA, or deciding whether an output can be called validated.

## Match method to question

| Question | Method | Main signals | Does not establish |
|---|---|---|---|
| How might people group and name items? | Open card sort | groupings, labels, disagreement | final IA |
| Do proposed categories make sense? | Closed/hybrid card sort | placement, ambiguity, new categories | full findability |
| Can people find destinations in a hierarchy? | Tree test | success, directness, path, time | interface quality |
| Is the first interface choice promising? | First-click test | first destination, confidence | complete task success |
| Can people complete real tasks? | Usability test | completion, errors, recovery, explanation | population-wide rates without design |
| What happens in production? | Analytics/search logs | paths, reformulation, zero results, exits | why it happens |

## Test tasks

Use realistic goals without copying navigation labels into the task. Include high-frequency, high-risk, cross-role, deep-entry, recovery, and edge-case tasks. Segment results where roles, expertise, language, or device plausibly affect behavior.

## Metrics

Choose a meaningful subset:

- task success;
- direct versus indirect success;
- first destination;
- wrong turns and backtracking;
- time to find;
- confidence and perceived control;
- recovery after error;
- search reformulation and zero results;
- browse versus search by task;
- deep-entry dead ends;
- orphan, duplicate, obsolete, and ownerless content;
- coverage by role, language, expertise, and context.

## Interpretation

Do not optimize click count in isolation. A longer path with clear labels may outperform a shorter ambiguous path. Diagnose label quality, competing choices, depth, task type, user knowledge, and recovery together.

## Validation plan template

```markdown
### Claim
What decision or assumption is being tested?

### Participants and segments
Who must be represented, and why?

### Method
Why does this method answer the claim?

### Tasks and materials
What will participants see and do?

### Measures and decision rule
What evidence would retain, revise, or reject the structure?

### Limitations
What will remain unknown?
```

Avoid universal sample-size claims. Select sample size from study purpose, variability, segmentation, risk, and practical constraints.

