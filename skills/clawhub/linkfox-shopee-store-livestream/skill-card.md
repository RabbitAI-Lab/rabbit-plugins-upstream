## Description:

Provides agent-facing access to 25 Shopee Open Platform Livestream APIs through LinkFox, including livestream session creation, start and end actions, item management, comments, metrics, and image upload.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and agent developers use this skill to manage authorized Shopee store livestream sessions, products, comments, metrics, and supporting media from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform Shopee store operations, billing/payment onboarding, and actions that may affect public livestream state.

Mitigation: Use it in a controlled workspace and require explicit user confirmation before public, destructive, or billing actions.

Risk: The skill handles API keys, account onboarding data, and phone or SMS-code flows.

Mitigation: Review endpoint environment variables before running and share phone or SMS codes through the agent only when intended.

Risk: Full API responses may be stored persistently and can contain store or account data.

Mitigation: Review saved response files before sharing workspaces or logs, and avoid exposing sensitive Shopee store data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-livestream)
- [Shopee Livestream API reference](https://open.shopee.com/documents/v2/v2.livestream.upload_image?module=125&type=1)
- [Livestream API module reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance, Files]

**Output Format:** [JSON API responses and summaries, plus Markdown-style operational guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Complete API responses are saved as local JSON files; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
