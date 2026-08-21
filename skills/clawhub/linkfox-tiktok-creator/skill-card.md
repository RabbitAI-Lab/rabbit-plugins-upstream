## Description:

Provides TikTok Shop creator profile, product, showcase, and shoppable-video API guidance through LinkFox creator API calls, requiring a creator access token from linkfox-tiktok-video-auth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operators and developers use this skill to query TikTok Shop creator profiles, creator-linked products, showcase products, and shoppable-video publishing or status APIs after obtaining a valid creator access token.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs real TikTok creator operations and requires creator access tokens.

Mitigation: Use only valid creator tokens, mask tokens in user-visible output, and review TikTok response codes before taking follow-up actions.

Risk: The skill can store TikTok creator and business API responses in the workspace.

Mitigation: Install or run it only where local storage of these responses is acceptable, and review saved files before sharing the workspace.

Risk: Endpoint environment variables can redirect calls to non-default LinkFox services.

Mitigation: Verify LinkFox endpoint environment variables are trusted before running API calls.

Risk: The onboarding flow can collect phone and SMS login details, generate API keys, create payment orders, and save payment QR files.

Mitigation: Use onboarding only when needed for authentication or billing, and confirm account, payment, and API-key handling with the user before proceeding.

## Reference(s):

- [TikTok Creator API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API request or response output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are written to a local linkfox session directory; large responses are summarized in stdout.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
