## Description:

Analyzes pet ear images or videos for visible ear-canal redness, dark granular discharge, earwax buildup, and related head-shaking or scratching indicators, then returns objective observations, abnormality alerts, and follow-up suggestions without providing a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, boarding centers, and veterinary pre-screening teams use this skill to analyze pet ear media for visible redness, discharge, earwax buildup, and head-shaking or scratching indicators. The skill produces objective health-reference observations, report links, and recommendations for owner review or veterinary follow-up rather than diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media, report history, workspace identity values, and access tokens may be sent to the configured cloud service or stored locally.

Mitigation: Review configured service endpoints and local state before running the skill; use a separate workspace or account for testing and avoid sensitive media unless this data flow is acceptable.

Risk: The skill silently creates or reuses an identity when associating analysis reports and history queries.

Mitigation: Use a dedicated workspace or account and review any existing local identity, token, or database files before running history queries.

Risk: Visual ear-health analysis can be mistaken for veterinary diagnosis.

Mitigation: Treat outputs as observations and follow-up guidance only; consult a veterinarian for concerning symptoms or treatment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-ear-health-snapshot-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Supplemental API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report text or JSON-style structured analysis, with optional saved output files and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include abnormality alerts, pet type, analysis timestamps, cloud report links, and Markdown history tables for prior reports.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter states 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
