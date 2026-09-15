## Description:

Operates Help Scout through OOMOL's oo CLI so an agent can read, create, and update Help Scout conversations, customers, inbox metadata, users, saved replies, workflows, tags, threads, and custom fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Support operators, customer success teams, and agents use this skill to inspect and manage Help Scout records through an OOMOL-connected account. It supports reading support data and performing confirmed updates such as replies, notes, assignments, statuses, tags, custom fields, snoozes, and manual workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands.

Mitigation: Verify the installer source independently or install the oo CLI through a trusted internal path before use.

Risk: Write actions can modify Help Scout business data, including replies, assignments, tags, custom fields, snoozes, and workflows.

Mitigation: Require explicit user confirmation of the target, payload, and intended effect before running any write action.

Risk: The Help Scout connection is mediated by OOMOL-managed credentials.

Mitigation: Use the skill only where trusting OOMOL with the Help Scout connection is acceptable for the organization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-helpscout)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Help Scout homepage](https://www.helpscout.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON data from Help Scout connector actions, including data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
