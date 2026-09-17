## Description:

Operate Klazify through the OOMOL-connected oo CLI to inspect action schemas and retrieve domain enrichment, company profile, logo, IAB category, similar-domain, social media, and technology-stack data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to run Klazify read actions through an OOMOL-connected account, including URL categorization, company data lookup, domain expiration lookup, logo retrieval, IAB classification, similar-domain discovery, social link lookup, and technology stack detection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer scripts that would run in a local shell.

Mitigation: Use an already installed or organization-approved oo CLI where possible; do not let an agent run curl-to-bash or PowerShell iex installers automatically, and review installation, login, connection, and billing steps before proceeding.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-klazify)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Klazify homepage](https://www.klazify.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect live action schemas before running connector actions and returns oo CLI JSON responses when actions are executed.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
