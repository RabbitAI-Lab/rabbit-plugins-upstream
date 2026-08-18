## Description:

ClinicalKey helps agents search and read ClinicalKey account data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve ClinicalKey account information through an OOMOL-connected account, including service status, usage reports, available reports, and consortium member data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected ClinicalKey account may expose sensitive institutional usage, report, or consortium member data.

Mitigation: Review the connected account scope before installing and share results only with users authorized to access that data.

Risk: The broad trigger language may route more ClinicalKey requests through the connector than a user expects.

Mitigation: Confirm user intent before retrieving account-level reports or member data, especially when the request is ambiguous.

## Reference(s):

- [ClinicalKey Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-clinicalkey)
- [ClinicalKey homepage](https://www.clinicalkey.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return ClinicalKey connector responses as JSON when actions are executed.]

## Skill Version(s):

1.0.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
