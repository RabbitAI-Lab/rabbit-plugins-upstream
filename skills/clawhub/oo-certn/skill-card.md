## Description:

Certn lets agents search and read Certn background-check cases, groups, users, packages, questionnaires, tags, and events through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Certn background-check resources through the OOMOL `oo` CLI without handling raw API tokens. It supports read-only retrieval and paginated listing for Certn cases, groups, users, packages, questionnaires, tags, and events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to execute remote installer scripts in a shell.

Mitigation: Review the installer path before installation and prefer a verified or signed oo CLI installation method.

Risk: A connected account can read Certn cases, users, groups, events, packages, questionnaires, and tags available to that OOMOL connection.

Mitigation: Use a least-privileged Certn/OOMOL connection and confirm the account scope before running connector actions.

## Reference(s):

- [ClawHub Certn skill page](https://clawhub.ai/oomol/skills/oo-certn)
- [Certn homepage](https://certn.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Certn connector actions return JSON data with meta.executionId; live action schemas should be checked before building payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
