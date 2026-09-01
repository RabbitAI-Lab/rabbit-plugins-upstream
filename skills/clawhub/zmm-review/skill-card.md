## Description:

Reviews talking-head scripts before publishing by scoring sentence-level information density, checking structure and red-line risks, and keeping the default output diagnostic rather than rewritten.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content operators use this skill to decide whether a talking-head script is ready to publish, what blocks publication, and which high-leverage lines or risks to fix first.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may store feedback and review calibration for future sessions without a clear opt-in or retention limit.

Mitigation: Review the memory and automatic write-back behavior before installing, and use a dedicated content vault that the agent is allowed to read and modify.

Risk: Draft scripts and unpublished content may be exposed to persistent review patterns or notes.

Mitigation: Avoid using the skill with confidential unpublished scripts unless that storage behavior is acceptable for the workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-review)
- [Publisher profile](https://clawhub.ai/user/iamzifei)
- [评分锚点](references/评分锚点.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown review report with scoring tables and concise diagnostic guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diagnose-only by default; may include targeted rewrite suggestions for red-line issues or when the user explicitly asks for edits.]

## Skill Version(s):

0.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
