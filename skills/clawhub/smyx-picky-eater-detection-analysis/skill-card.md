## Description:

Analyzes pet feeding-area videos or video URLs for selective eating behavior and provides feeding observations and suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and staff at smart-feeder services, boarding facilities, or veterinary wards use the skill to identify selective eating patterns in feeding-area videos and review feeding suggestions or past reports. Results are behavioral observations, not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Feeding videos or video URLs are sent to configured external services.

Mitigation: Confirm the service endpoints and obtain appropriate consent before submitting sensitive home, boarding, or hospital footage.

Risk: The skill may create or reuse an account identity and retain reusable authentication tokens in local workspace data.

Mitigation: Review the local identity, database, and token storage before installation; restrict access to the workspace data directory.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-picky-eater-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [JSON or Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links to cloud reports or an optional saved result file.]

## Skill Version(s):

1.0.9 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
