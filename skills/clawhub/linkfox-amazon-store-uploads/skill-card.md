## Description:

Creates Amazon SP-API upload destinations and uploads files to the returned pre-signed URL for A+ Content, Messaging, and related store workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators and developers use this skill to create Amazon upload destinations, upload matching file bytes, and pass the resulting upload destination ID to A+ Content, Messaging, or similar SP-API workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys, phone-number based login, and upload URLs.

Mitigation: Install only when LinkFox is trusted for this workflow, keep API keys and upload URLs out of shared logs, and rotate credentials if they are exposed.

Risk: Billing recovery can initiate payment orders when quota or balance errors occur.

Mitigation: Confirm the selected plan, payment method, and order details with the user before creating an order or displaying payment artifacts.

Risk: Full API responses are saved to local linkfox response files.

Mitigation: Treat saved response files as sensitive, review their storage location, and delete them when they are no longer needed.

Risk: Endpoint-related environment variables can change where requests are sent.

Mitigation: Review LinkFox gateway and API endpoint environment variables before use, especially in shared or managed environments.

## Reference(s):

- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [Amazon createUploadDestinationForResource](https://developer-docs.amazon.com/sp-api/reference/createuploaddestinationforresource)
- [Amazon Create an upload destination](https://developer-docs.amazon.com/sp-api/docs/create-an-upload-destination)
- [Amazon Messaging API v1 Reference](https://developer-docs.amazon.com/sp-api/docs/messaging-api-v1-reference)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-uploads)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON, files]

**Output Format:** [Markdown guidance with shell commands and JSON responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full LinkFox responses under a linkfox session directory and print either the full JSON or a summary depending on response size and inline mode.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
