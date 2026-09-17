## Description:

Use this skill to access IPQualityScore (ipqualityscore.com) for IP, URL, email, and phone risk or validation checks through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect IPQualityScore connector schemas and run IP, URL, email, and phone reputation or validation checks through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Do not allow an agent to run those installer commands automatically; install the CLI from a trusted, verified source and review setup commands before execution.

Risk: IPQualityScore requests are brokered through OOMOL using server-side credentials.

Mitigation: Use this skill only when the user is comfortable with OOMOL brokering IPQualityScore requests through the connected account.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [IPQualityScore homepage](https://www.ipqualityscore.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
