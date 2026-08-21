## Description:

Retrieves patent abstract drawing image paths from the Zhihuiya patent database by patent ID or publication number.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and patent-focused teams use this skill to look up abstract drawing images for one or more patents by ID or publication number and receive image links or Markdown display guidance. The skill is limited to abstract image retrieval and does not provide patent search, claims analysis, legal status, valuation, or infringement analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a paid LinkFox/Zhihuiya integration and may consume account quota or prompt payment flows.

Mitigation: Confirm expected token or point cost with the user before additional lookups, and require explicit approval before any plan purchase or payment action.

Risk: Authentication and onboarding flows may handle phone numbers, SMS codes, API keys, account state, and payment QR codes.

Mitigation: Prefer self-service API-key setup, avoid routing OTPs through an agent unless necessary, and do not expose API keys in chat, logs, or shared files.

Risk: The skill writes full API responses and cached results to local files, which may include patent lookup details and account-related metadata.

Mitigation: Run it only in an appropriate workspace, review generated linkfox data/cache files, and remove local artifacts when they are no longer needed.

Risk: Automatic feedback reporting may transmit user feedback text or task context to the publisher's feedback endpoint.

Mitigation: Review or redact feedback content before submission when it could contain sensitive business, patent, or account information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-abstract-image)
- [智慧芽-摘要附图 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown summaries with image links, JSON API responses, and local JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts patentId or patentNumber input, supports batches up to 100 values, caches identical requests for 24 hours, and may summarize responses larger than 8 KB unless inline output is requested.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
