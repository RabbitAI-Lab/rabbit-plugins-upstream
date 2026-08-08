## Description:

Creates Amazon SP-API Uploads API destinations through LinkFox, computes or accepts contentMD5 values, uploads files to returned upload URLs, and guides authentication or billing recovery when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, operators, and agents use this skill to prepare binary files for Amazon A+ Content, Messaging, or similar workflows by creating upload destinations and PUT-uploading matching bytes. It is intended for users who already have an Amazon seller context, a LinkFox API key, and the companion store-auth skill for seller and region selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Amazon store workflow data and upload destinations through LinkFox services.

Mitigation: Install and run it only when LinkFox is trusted for the relevant Amazon seller workflow and verify sellerId, region, marketplaceId, resource, contentMD5, and contentType before execution.

Risk: Authentication flows can request phone/SMS login and generate or expose LinkFox API keys.

Mitigation: Use onboarding commands only after the user explicitly initiates them, keep API keys out of shared logs, and prefer environment-variable configuration over pasting keys into prompts.

Risk: Billing flows can list paid plans and create payment orders.

Mitigation: Run payment commands only with explicit user consent, confirm the selected plan and payment method before order creation, and avoid polling payment status automatically.

Risk: Saved response files may contain sensitive upload URLs, headers, order data, or other workflow details.

Mitigation: Review the ./linkfox session output directory after use and remove persisted files when the workspace should not retain that data.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-uploads)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [Amazon createUploadDestinationForResource](https://developer-docs.amazon.com/sp-api/reference/createuploaddestinationforresource)
- [Amazon Create an upload destination](https://developer-docs.amazon.com/sp-api/docs/create-an-upload-destination)
- [Amazon Messaging API reference](https://developer-docs.amazon.com/sp-api/docs/messaging-api-v1-reference)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands, JSON stdout, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default script behavior saves full JSON responses under ./linkfox/<date>/<session>/data; small responses are printed in full, large responses are summarized unless --inline is used.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
