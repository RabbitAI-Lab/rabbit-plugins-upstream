## Description:

Prospeo lets agents search and read Prospeo company and person data through an OOMOL-connected oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to enrich companies or people, search Prospeo company and people data, retrieve autocomplete suggestions, and check Prospeo account information through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup fallback can run an unverified internet installer for the oo CLI.

Mitigation: Use a pinned, documented installer with checksum or signature verification and explicitly approve any local software installation.

Risk: Prospeo access depends on OOMOL acting as an intermediary for connector execution and credentials.

Mitigation: Install and use the skill only when that intermediary model is acceptable for the user's Prospeo account and organization policy.

## Reference(s):

- [ClawHub Prospeo Skill](https://clawhub.ai/oomol/skills/oo-prospeo)
- [Prospeo Homepage](https://prospeo.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing JSON payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
