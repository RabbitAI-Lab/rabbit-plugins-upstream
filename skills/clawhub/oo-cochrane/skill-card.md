## Description:

Cochrane connector skill for searching and reading Cochrane review data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Cochrane connector action schemas and retrieve review metadata, document roles, translations, and version history through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can execute remote installer scripts without checksum or signature verification.

Mitigation: Use a verified oo CLI package or independently validate the installer source before running it with local account privileges.

Risk: Connector requests depend on live action schemas and authenticated account state.

Mitigation: Inspect the current action schema before constructing each payload and only run setup or connection steps after an auth or connection failure.

## Reference(s):

- [Cochrane Homepage](https://www.cochrane.org)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-cochrane)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [Skill Icon](https://static.oomol.com/logo/third-party/cochrane.png)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only connector actions return JSON data with execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
