## Description:

Temu Global ecommerce ads skill that routes Partner Global Ads API requests through the LinkFox gateway for ad creation, modification, ROAS prediction, reporting, logs, and signed file downloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu Global sellers, operators, and developers use this skill to manage LinkFox-mediated Temu Partner Ads workflows, including creating and modifying ads, checking eligible goods, predicting ROAS, reviewing reports, and inspecting logs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires LinkFox and Temu credentials and can read or write local token files.

Mitigation: Store credentials only in private, unsynced locations, restrict file permissions, and rotate or remove tokens when access is no longer needed.

Risk: The skill can create, delete, pause, reopen, and change budgets or ROAS for live ads.

Mitigation: Require explicit human confirmation before any ad-management action that changes campaign state, spend, or ROAS targets.

Risk: The skill performs broad LinkFox gateway proxying and signed file downloads.

Mitigation: Verify gateway URLs are official LinkFox hosts and review request payloads and download URLs before execution.

Risk: The skill persists full API responses locally, which may include sensitive store or advertising data.

Mitigation: Review saved response paths, avoid shared or synced directories, and delete response files that are not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-ads-global)
- [API reference](references/api.md)
- [Temu accessToken authorization and retrieval](references/access-token.md)
- [Partner Global Ads catalog](references/partner-global-catalog.md)
- [Ads API documentation index](references/apis/README.md)
- [Onboarding and account guidance](references/onboarding.md)
- [Temu Partner Global documentation](https://partner-global.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance, shell command examples, JSON API responses, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under linkfox/<date>/<session>/data; responses over 8 KB are summarized unless --inline is used.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
