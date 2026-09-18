## Description:

Enables agents to search and retrieve Gangtise market, company research, and fundamentals data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to access Gangtise financial-market data, company research, announcements, meeting summaries, and broker research through schema-checked OOMOL connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance includes remote shell and PowerShell installer commands for the oo CLI.

Mitigation: Review and verify the installer or use a trusted package-manager or versioned installer path before authenticating.

Risk: The skill depends on OOMOL account authentication, Gangtise connection status, and available OOMOL billing credits.

Mitigation: Run setup or recovery steps only after connector commands fail with authentication, connection, scope, expiration, app, or billing errors.

Risk: Connector payloads can be malformed or target the wrong securities if action schemas are assumed.

Mitigation: Fetch the live action schema with `oo connector schema` before constructing each `oo connector run` payload.

## Reference(s):

- [Gangtise homepage](https://www.gangtise.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gangtise)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON connector payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Gangtise connector results returned as JSON data with execution metadata.]

## Skill Version(s):

1.0.2 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
