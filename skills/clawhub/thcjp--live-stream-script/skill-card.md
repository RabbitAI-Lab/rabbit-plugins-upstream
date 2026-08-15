## Description:

流 helps agents draft Chinese live-stream scripts for e-commerce, entertainment, and educational broadcasts, including opening warmups, interaction prompts, and conversion-oriented talking points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, operators, and marketing teams use this skill through an AI agent to draft Chinese live-stream scripts, interaction flows, and promotional talking points from basic content, mode, and style inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan rates the skill as suspicious because it declares read, write, and command execution access broader than its live-stream drafting purpose.

Mitigation: Review before installation and restrict read, write, and command execution permissions at the agent or platform level.

Risk: The artifact describes command execution support without a tight operational scope.

Mitigation: Supervise command use, allow only necessary commands, and avoid passing untrusted user input directly into shell commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/live-stream-script)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [SkillHub homepage from artifact metadata](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown or JSON responses containing generated live-stream script content and metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include Chinese script text, interaction prompts, opening warmups, conversion talking points, and response metadata.]

## Skill Version(s):

1.0.0 (source: ClawHub server release metadata; artifact frontmatter declares 2.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
