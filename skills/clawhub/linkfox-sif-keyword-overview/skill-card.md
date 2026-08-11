## Description:

This skill queries LinkFox SIF keyword overview data to help Amazon sellers analyze keyword-level competition, search volume, advertising presence, and supply-demand ratios across supported marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and marketplace analysts use this skill to request LinkFox SIF keyword metrics and present objective competition, search-volume, ad-count, and supply-demand summaries for product research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a LinkFox API key and sends Amazon keyword queries to LinkFox services.

Mitigation: Use the skill only when the user accepts sharing those queries with LinkFox and keep API keys in approved credential storage or scoped environment variables.

Risk: The onboarding flow may collect a phone number and SMS code, issue or reveal an API key, create payment orders, and display payment QR codes.

Mitigation: Review onboarding prompts before proceeding, confirm any billing action with the user, and avoid exposing SMS codes or generated credentials outside the trusted flow.

Risk: Custom LinkFox gateway URL environment variables can redirect requests to a different endpoint.

Mitigation: Leave custom gateway overrides unset unless the endpoint has been reviewed and approved.

Risk: Saved LinkFox output directories may contain business-sensitive keyword research data or credentials.

Mitigation: Treat saved outputs as sensitive and apply appropriate workspace access, retention, and cleanup controls.

Risk: Automatic feedback reporting can send information about skill behavior or user reactions to LinkFox.

Mitigation: Review feedback content before submission when the workflow surfaces feedback-worthy events.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sif-keyword-overview)
- [SIF keyword overview API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request and response data plus optional shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses to a local linkfox data directory; responses over 8 KB are summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
