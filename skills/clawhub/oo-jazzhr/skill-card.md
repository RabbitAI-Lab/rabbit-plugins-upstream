## Description:

JazzHR lets agents search and read JazzHR recruiting data through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve JazzHR applicants, jobs, and users through an OOMOL-connected account while checking live action schemas before requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that may execute changing external code.

Mitigation: Install the oo CLI through an official, versioned route and verify checksums or signatures before use.

Risk: JazzHR requests may expose recruiting and HR data through OOMOL-connected services.

Mitigation: Use the skill only where routing JazzHR read requests through OOMOL aligns with organizational HR data policies.

## Reference(s):

- [JazzHR homepage](https://www.jazzhr.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub JazzHR skill page](https://clawhub.ai/oomol/skills/oo-jazzhr)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and PowerShell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON payloads and JSON responses for oo connector actions.]

## Skill Version(s):

1.0.2 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
