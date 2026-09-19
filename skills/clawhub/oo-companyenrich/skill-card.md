## Description:

CompanyEnrich helps agents search companies, enrich company profiles, find similar companies, and retrieve the authenticated user's CompanyEnrich account summary through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query CompanyEnrich data from an OOMOL-connected account for company search, profile enrichment, similar-company discovery, and account capability checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance may run unverified installer code from the internet.

Mitigation: Install the oo CLI only through a verified, version-pinned, checksum- or signature-validated method, and require explicit user approval before an agent runs installer commands.

## Reference(s):

- [CompanyEnrich homepage](https://companyenrich.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-companyenrich)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
