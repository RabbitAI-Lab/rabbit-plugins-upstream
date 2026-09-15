## Description:

IPLocate provides agent access to IP geolocation, ASN, privacy, hosting, company, and abuse lookups through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up IPLocate IP intelligence data through an OOMOL-connected account, including single IP, batch IP, and connector-server outgoing IP lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented first-time setup includes remote shell installer commands for the oo CLI.

Mitigation: Do not run installer commands automatically; review OOMOL's installer channel and prefer a verified, signed, or package-manager installation path.

## Reference(s):

- [ClawHub IPLocate Skill](https://clawhub.ai/oomol/skills/oo-iplocate)
- [IPLocate Homepage](https://www.iplocate.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-focused IPLocate actions; batch lookup responses preserve per-IP inline errors when returned.]

## Skill Version(s):

1.0.3 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
