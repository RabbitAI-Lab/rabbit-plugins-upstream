## Description:

Queries SellerSprite traffic keywords for an Amazon ASIN, including keyword traffic sources, traffic share type, conversion type, organic rank, ad rank, historical months, and sorting options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce analysts use this skill to inspect the keyword traffic structure for an Amazon ASIN, including organic and advertising positions, traffic share, and conversion categories. Agents can also guide users through LinkFox authentication or billing setup when the API key or paid credits are missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide phone/SMS login, API-key generation, and paid credit purchases through LinkFox/SellerSprite flows.

Mitigation: Install and use it only when those account and billing actions are expected; confirm user intent before actions that consume credits or create orders.

Risk: Credential-bearing endpoints are configurable through environment variables.

Mitigation: Use only official LinkFox endpoint environment variables and review any environment overrides before running the scripts.

Risk: Full keyword responses are saved locally and may contain sensitive business research data.

Mitigation: Treat saved linkfox data files as sensitive, review them before sharing, and delete them when retention is not needed.

Risk: API keys may be persisted in shell profile instructions during onboarding.

Mitigation: Prefer temporary or managed secret storage when possible, and avoid committing shell profiles or saved output files that contain credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sellersprite-traffic-keyword)
- [卖家精灵-流量词反查 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration, guidance]

**Output Format:** [JSON API responses, saved JSON files, concise text summaries, and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The lookup script caches identical requests for 24 hours, saves full responses under a local linkfox session directory, and prints a compact summary when responses exceed 8 KB unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
