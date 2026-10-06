## Description:

Analyzes submitted pet-ear photos or videos for visible redness, discharge, and earwax, returning observations, alerts, and guidance rather than a veterinary diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, boarding staff, and veterinary intake teams use the skill to review ear imagery for visible concerns and retrieve prior analysis reports. Results are observational and do not replace a veterinarian's examination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media may be uploaded to or referenced by a cloud service, and account-linked report history may be stored there.

Mitigation: Use only if you trust the lifeemergence.com service and have permission to share the media and retain account-linked reports.

Risk: The skill silently creates or reuses an account and stores returned authentication tokens in a local workspace SQLite database.

Mitigation: Review local data and token handling before installation, and restrict access to the workspace and its stored credentials.

Risk: Visual observations can be mistaken for a diagnosis of an ear condition.

Mitigation: Treat findings as preliminary observations and consult a veterinarian about concerning symptoms.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-ear-health-snapshot-analysis)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis report or Markdown table of historical reports; optional saved text file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include visible findings, alerts, recommendations, and report links; not a medical diagnosis]

## Skill Version(s):

1.0.11 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
