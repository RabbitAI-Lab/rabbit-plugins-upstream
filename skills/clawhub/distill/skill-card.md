## Description:

Session knowledge distillation assigns what an agent learned in a session into a four-layer persistent knowledge base: rules, memory, skills, and decision records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill at the end of a session to decide which lessons should become durable rules, memories, reusable skills, or decision records. It is intended for workflows that already maintain these persistent knowledge layers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect placement of persistent knowledge can cause future agent sessions to inherit the wrong guidance.

Mitigation: Review the chosen scope, layer, paths, and memory bucket before saving any distilled knowledge.

Risk: Duplicating or padding rules, memories, or skills can make the knowledge base harder to trust and maintain.

Mitigation: Search existing knowledge artifacts first, update existing entries when covered, and omit low-value items.

Risk: Knowledge-base edits may accidentally include unrelated in-progress workspace changes.

Mitigation: Check workspace status and stage only the specific files changed by the distillation.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown allocation table with concise rationale]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes what was added, where it was placed, and what was intentionally left out.]

## Skill Version(s):

2.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
