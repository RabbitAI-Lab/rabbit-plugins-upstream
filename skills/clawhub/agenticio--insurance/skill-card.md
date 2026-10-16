## Description:

Local-first insurance record organizer for storing policy details, listing policies, tracking renewal dates, logging claim events, and summarizing insurance records without providing insurance advice or facilitating purchases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticio](https://clawhub.ai/user/agenticio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to organize already-known insurance records in a local workspace: policy details, renewal tracking, claim event logs, and simple summaries. It is not for insurance advice, coverage recommendations, legal interpretation, or purchasing policies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive policy numbers, insured names, premiums, coverage limits, deductibles, and claim details are stored as plaintext local JSON files.

Mitigation: Use the skill only in a private workspace, restrict filesystem access, and avoid entering unnecessary sensitive details.

Risk: Local records and corruption backups may remain readable after use unless retention and deletion are managed.

Mitigation: Review and delete obsolete files under memory/insurance/, including backup files, according to the user's retention needs.

Risk: The skill is for record organization and could be mistaken for insurance or legal advice.

Mitigation: Keep use limited to stored-record organization and consult licensed professionals for coverage decisions, policy interpretation, or legal questions.

## Reference(s):


## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [JSON command output and concise natural-language guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local JSON records under memory/insurance/; no external APIs are described.]

## Skill Version(s):

2.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
