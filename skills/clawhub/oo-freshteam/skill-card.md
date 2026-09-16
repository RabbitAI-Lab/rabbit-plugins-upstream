## Description:

Freshteam enables agents to search and read Freshteam employee and recruiting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, recruiting operators, and developers use this skill to retrieve Freshteam employee directory data, job postings, applicant fields, candidate sources, and related recruiting metadata from a connected Freshteam account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running an unverified internet installer directly in a shell.

Mitigation: Prefer a verified or package-manager installation method for the oo CLI before using the skill.

Risk: Freshteam employee and recruiting data passes through the OOMOL connector.

Mitigation: Use the skill only if OOMOL and the oo CLI are trusted, and connect Freshteam with the minimum permissions needed.

## Reference(s):

- [ClawHub Freshteam Skill](https://clawhub.ai/oomol/skills/oo-freshteam)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Freshteam Homepage](https://www.freshworks.com/freshteam/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing Freshteam requests.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
