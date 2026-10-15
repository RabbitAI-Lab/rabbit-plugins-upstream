## Description:

Looks up IP addresses, autonomous systems, and countries in Greip through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can retrieve Greip IP, ASN, and country information through an OOMOL-connected account without handling raw Greip API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the OOMOL connector sends Greip lookup requests through an intermediary.

Mitigation: Use only if comfortable with OOMOL as the intermediary, and connect only the credentials and scopes needed for lookups.

Risk: The first-time setup examples pipe a remote installer into a shell.

Mitigation: Review OOMOL's official installation guidance and verify the installer source before running it.

## Reference(s):

- [Greip](https://greip.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Greip skill on ClawHub](https://clawhub.ai/oomol/skills/oo-greip)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance and structured JSON lookup results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [IP, ASN, and country lookup details depend on the selected action and its live schema.]

## Skill Version(s):

1.0.0 (source: skill metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
