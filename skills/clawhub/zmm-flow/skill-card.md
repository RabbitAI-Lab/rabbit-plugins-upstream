## Description:

Analyzes talking-head scripts to identify likely audience drop-off points caused by logic gaps, density dips, or hard-to-speak sentences, then asks whether to produce a marked-up revision.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and their agents use this skill to review talking-head scripts for retention risks in paragraph transitions, information density, and spoken fluency. It returns a concise diagnosis and can guide a marked-up rewrite while preserving the user's original argument and voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read local style/reference memory and save future correction or performance notes without clear user opt-in.

Mitigation: Require explicit confirmation before memory writes and limit reads to zmm-flow-specific memory unless broader continuity is intentionally desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-flow)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report with optional marked-up script edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include paragraph structure, risk labels, quoted script excerpts, speakable fixes, and revision prompts.]

## Skill Version(s):

0.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
