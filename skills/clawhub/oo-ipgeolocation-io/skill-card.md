## Description:

IPGeolocation.io operates IPGeolocation.io through an OOMOL-connected account for IP geolocation, timezone, and astronomy queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run IPGeolocation.io lookups through an OOMOL-connected account, including IP geolocation, timezone, and astronomy queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI only through a trusted, verified, user-controlled method; do not let an agent automatically run remote installer scripts.

Risk: Account setup and connector authorization can affect access to an external service.

Mitigation: Confirm sign-in, connection, scope, and billing steps with the user before performing setup or retrying failed authorization flows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-ipgeolocation-io)
- [IPGeolocation.io Homepage](https://ipgeolocation.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
