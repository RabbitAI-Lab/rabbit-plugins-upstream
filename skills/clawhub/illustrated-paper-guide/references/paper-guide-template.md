# Paper Guide and Checklist Template

Use this template as a strong default, then adapt section depth to the paper and
the reader's goal.

## README.md

```markdown
# [Paper title]: illustrated study guide

> This is a study guide, not the original paper.
> Reading progress: [CHECKLIST.md](./CHECKLIST.md)

<a id="ckpt-bp1"></a>
## BP1 Problem: what is this paper trying to solve?

[Motivation, gap, and the question in plain language.]

<a id="ckpt-bp2"></a>
## BP2 Method: what did the authors do?

[Subjects/data, intervention or model, comparisons, and measurements.]

<a id="ckpt-bp3"></a>
## BP3 Conclusion: what should I remember?

[Three to six main results and one overall claim.]

<a id="ckpt-bp4"></a>
## BP4 Reading map

[Where a shallow pass ends and which sections support each major claim.]

<a id="ckpt-a1"></a>
## A1 Paper information

| Field | Value |
| --- | --- |
| Title | |
| Authors | |
| Venue and year | |
| DOI or canonical URL | |

[Continue with A-F sections appropriate to the paper.]
```

## CHECKLIST.md

```markdown
# Reading checklist: [short paper title]

> Main guide: [README.md](./README.md)

## Big Picture

- [ ] [BP1 Problem: what is this paper trying to solve?](./README.md#ckpt-bp1)
  **Done when:** I can explain the gap without reading the abstract.

- [ ] [BP2 Method: what did the authors do?](./README.md#ckpt-bp2)
  **Done when:** I can name the data or subjects, comparison, and measurement.

- [ ] [BP3 Conclusion: what should I remember?](./README.md#ckpt-bp3)
  **Done when:** I can state the main result without overstating causality.

- [ ] [BP4 Reading map](./README.md#ckpt-bp4)
  **Done when:** I know which section to read next for my goal.
```

## Stable Anchor Rules

- Put `<a id="ckpt-code"></a>` immediately above the linked heading.
- Start the heading with the same code used by the anchor.
- Keep the checklist label and heading identical character for character.
- Use one checkpoint per testable learning outcome, not per paragraph.
- If a heading changes, update the heading, anchor, and checklist together.

## Completion Criteria Patterns

Prefer observable outcomes:

- “I can draw the causal chain from memory.”
- “I can identify the control and explain why it matters.”
- “I can point to the panel region supporting the claim.”
- “I can separate the measured result from the authors' interpretation.”

Avoid vague outcomes such as “I understand this section.”
