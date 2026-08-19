## Description:

Provides agent guidance for searching and reading ClinicalTrials.gov data through OOMOL's clinicaltrials_gov connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search ClinicalTrials.gov studies, retrieve study records by NCT ID, and inspect eligibility, locations, documents, results, metadata, registry statistics, and related public study data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClinicalTrials.gov queries are routed through OOMOL's oo CLI.

Mitigation: Use an expected OOMOL account, run installer or login steps only when needed, and review payloads before execution.

Risk: Connector action schemas or payload requirements may change over time.

Mitigation: Inspect the live action schema with oo connector schema before sending a payload.

## Reference(s):

- [ClinicalTrials.gov](https://clinicaltrials.gov/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-clinicaltrials-gov)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON payload or response handling.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
