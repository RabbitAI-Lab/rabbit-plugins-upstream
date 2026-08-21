## Description:

Analyzes pet ear images, videos, or URLs for visual indicators such as ear-canal color, discharge, earwax accumulation, and scratching or head-shaking context, then returns structured observations, alerts, care suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners, boarding centers, and veterinary intake teams use this skill to submit pet ear media for visual health screening and retrieve structured current or historical reports. Results are intended as visual observations and care guidance, not medical diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet ear media, submitted URLs, generated analysis records, and report history are sent to the vendor service.

Mitigation: Use only media that is appropriate to share with the vendor service, and review privacy, retention, and consent expectations before use in shared, clinical, boarding, or multi-user settings.

Risk: The skill creates or reuses an automatically managed local identity and persists authentication tokens locally.

Mitigation: Run the skill in a dedicated workspace, protect local data files and databases, and clear or rotate stored identity and token data when decommissioning or transferring the workspace.

Risk: The output is based on visual analysis and may be incomplete or misleading if used as a diagnosis.

Mitigation: Treat results as preliminary observations and care guidance; seek veterinary review for persistent symptoms, abnormal discharge, redness, pain, odor, or behavior changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-ear-health-snapshot-analysis)
- [Pet Ear Health API Interface Documentation](references/api_doc.md)
- [Shared Analysis API Error Codes](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON content, status messages, and report links; output can optionally be saved to a file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include historical report lists and vendor report export links.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
