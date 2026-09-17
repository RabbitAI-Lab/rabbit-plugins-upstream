## Description:

Appcues lets agents read, list, publish, and unpublish Appcues flows and content tags through the oo CLI for a connected OOMOL account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Appcues content from an agent workflow, including inspecting flows and tags and performing controlled publish or unpublish actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can install software from a network location if followed during setup.

Mitigation: Use a trusted, verifiable oo CLI installation path and review the installer source before execution.

Risk: Publishing or unpublishing Appcues flows can change customer-facing product experiences.

Mitigation: Require explicit confirmation of the Appcues account, flow identifier, payload, and expected effect before running publish or unpublish actions.

Risk: The release evidence marks the skill security verdict as suspicious.

Mitigation: Review the skill and security guidance before installation or deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-appcues)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Appcues homepage](https://www.appcues.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke Appcues connector actions through a connected OOMOL account; state-changing operations require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
