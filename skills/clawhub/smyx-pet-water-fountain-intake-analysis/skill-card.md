## Description:

Analyzes pet water-fountain videos or URLs through a remote service to produce drinking frequency, session duration, estimated daily intake, baseline comparison, abnormal change alerts, and report links for pet health monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and smart-pet-care operators use this skill to analyze water-fountain media, review structured drinking metrics, and retrieve historical drinking reports. The output supports monitoring and early warning workflows, but it should not be treated as veterinary diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet or home media and report history are sent to a remote service for analysis and historical report lookup.

Mitigation: Install only when that data sharing is acceptable, and avoid submitting sensitive or unnecessary media.

Risk: The security evidence flags under-scoped identity, credential, billing, and cleartext network behavior.

Mitigation: Review the publisher and service configuration before use; prefer HTTPS endpoints and secure credential storage for any deployment.

Risk: The skill presents estimated intake changes that may be mistaken for medical conclusions.

Mitigation: Use the reports as health-monitoring signals only and refer concerning changes to a veterinarian.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-water-fountain-intake-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Pet water fountain analysis API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis report with status text, metrics, alerts, suggestions, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include remote report URLs and historical report tables; intake amounts are estimates derived from observed drinking events and durations.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter declares 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
