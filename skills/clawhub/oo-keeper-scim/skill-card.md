## Description:

Enables an agent to read Keeper SCIM users, groups, and service provider configuration through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, IT administrators, and support agents use this skill to retrieve Keeper SCIM users, groups, and service provider configuration from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands that can execute code from URLs.

Mitigation: Do not let an agent run those installers automatically; install the OOMOL CLI only from a verified source with user approval, preferably with a pinned release and checksum or signature verification.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-keeper-scim)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Keeper SCIM](https://www.keepersecurity.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing Keeper SCIM read requests.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
