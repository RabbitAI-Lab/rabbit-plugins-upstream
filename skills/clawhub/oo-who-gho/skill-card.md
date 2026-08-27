## Description:

WHO Global Health Observatory helps agents search WHO GHO indicators and retrieve read-only health data through the OOMOL who_gho connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to search WHO Global Health Observatory indicators and retrieve read-only observations with dimension and year filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: WHO GHO requests are routed through the OOMOL oo CLI, so use depends on the CLI being installed and signed in when required.

Mitigation: Run connector actions directly when available, and use the documented first-time setup steps only after a command fails for a matching installation or authentication reason.

Risk: Connector access may stop on OOMOL billing or credit errors.

Mitigation: Treat HTTP 402 or OOMOL_INSUFFICIENT_CREDIT responses as a billing stop and resolve account credit before retrying.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-who-gho)
- [WHO Global Health Observatory homepage](https://www.who.int/data/gho)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include connector response JSON containing WHO GHO data and execution metadata.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
