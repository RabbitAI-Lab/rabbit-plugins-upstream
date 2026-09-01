## Description:

Analyzes Chinese talking-head scripts for likely viewer drop-off points by checking paragraph logic, information density, and speakability, then offers marked-up revision support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators use this skill to review knowledge-video talking-head scripts for retention risks and get concrete, speakable fixes before recording.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can save user-specific draft feedback, rejected rewrite preferences, and retention or performance notes in persistent memory.

Mitigation: Review memory behavior before installing, use it only in workspaces intended for the same user, and avoid installation where persistent writing feedback is not acceptable.

Risk: The skill depends on referenced zmm guidance files and memory directories for its operating rules.

Mitigation: Install it only where the referenced zmm files and memory directory exist and are intended for this user's workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-flow)
- [ClawHub publisher profile](https://clawhub.ai/user/iamzifei)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown review report with quoted script excerpts and optional marked-up revision guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk labels, segment tables, before-and-after rewrite markings, and a numbered next-step choice.]

## Skill Version(s):

0.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
