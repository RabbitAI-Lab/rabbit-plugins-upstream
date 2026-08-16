## Description:

Shopee store authorization and management skill for generating ERP or Ads authorization URLs, checking authorized stores, and reading authorization status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce operators use this skill to connect Shopee stores to LinkFox workflows, distinguish ERP and Ads authorization, and confirm store authorization state before using downstream Shopee skills.

### Deployment Geography for Use:

Global; the skill documents Shopee authorization regions cn, global, and br.

## Known Risks and Mitigations:

Risk: The skill can guide account login, API-key generation, and billing or payment flows beyond Shopee authorization.

Mitigation: Use those flows only when intentionally onboarding or resolving billing with LinkFox, and avoid entering phone numbers, SMS codes, or payment choices through the agent otherwise.

Risk: The skill saves full API responses and authorization URL files locally.

Mitigation: Review and clear generated linkfox session files and saved authorization URLs after use, especially on shared machines or workspaces.

Risk: Shopee ERP and Ads authorization are separate, and using the wrong application type can cause failed or unintended downstream access.

Mitigation: Confirm the intended appType before generating authorization URLs and verify shopId or merchantId together with appType before downstream Shopee operations.

## Reference(s):

- [Shopee authorization API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-auth)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses, status summaries, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses may be saved under a linkfox session directory; large responses may be summarized unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
