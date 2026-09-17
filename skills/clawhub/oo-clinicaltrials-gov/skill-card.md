## Description:

ClinicalTrials.gov (clinicaltrials.gov). Use this skill for ANY ClinicalTrials.gov request - searching and reading data. Whenever a task involves ClinicalTrials.gov, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search ClinicalTrials.gov and retrieve official study records, eligibility, locations, documents, results, registry statistics, API metadata, enumeration values, and search-area definitions through OOMOL's ClinicalTrials.gov connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer snippets that run directly in a shell.

Mitigation: Use an official reviewed installer or a version-pinned, integrity-verified installation path before using the connector.

Risk: ClinicalTrials.gov query payloads and account or execution metadata are handled through OOMOL.

Mitigation: Install and use the skill only when that data handling model is acceptable for the user's environment.

## Reference(s):

- [ClinicalTrials.gov](https://clinicaltrials.gov/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-clinicaltrials-gov)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON data with execution metadata when actions are run.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
