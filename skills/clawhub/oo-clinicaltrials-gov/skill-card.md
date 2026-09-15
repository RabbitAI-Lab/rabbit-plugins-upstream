## Description:

ClinicalTrials.gov helps agents search and retrieve ClinicalTrials.gov study data through the OOMOL clinicaltrials_gov connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and clinical research operations teams use this skill to search ClinicalTrials.gov and retrieve study records, eligibility, locations, documents, results, metadata, statistics, and API details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask an agent to run a remotely downloaded oo CLI installer directly in a shell.

Mitigation: Review and approve CLI installation manually, prefer a verified or pinned installation method, and avoid unattended pipe-to-shell execution.

Risk: ClinicalTrials.gov requests are mediated through OOMOL infrastructure.

Mitigation: Install and use the skill only when use of OOMOL as an intermediary is acceptable for the intended data workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-clinicaltrials-gov)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [ClinicalTrials.gov Homepage](https://clinicaltrials.gov/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector actions that return JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
