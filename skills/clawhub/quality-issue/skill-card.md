## Description:

从 Amazon 低星评论和商品字段中归纳产品质量问题线索、证据和优先级；仅用于质量问题线索，不替代质检、认证、召回或供应商执行。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon operators and product teams use this skill to identify product quality issue signals from low-star reviews, product fields, and ARI reports. It supports quality triage and operational decision-making, not formal quality certification, recall decisions, supplier enforcement, or true return-rate accounting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags this release as suspicious because it can store an ARI API key, spend credits under auto-confirm rules, and change account monitoring or workflow settings.

Mitigation: Install only when the publisher and ARI service are trusted; keep auto-confirm set to ask for approval when per-action credit review is needed.

Risk: A custom ARI endpoint can expose Amazon product, review, report, or account data to an unintended service.

Mitigation: Use the default trusted HTTPS ARI endpoint unless the custom ARI_BASE_URL is controlled and intentionally configured.

Risk: Exports may overwrite existing local files.

Mitigation: Review export paths before running export commands and choose a destination where overwrites are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/quality-issue)
- [Operation workflow reference](artifact/references/operation-workflow.md)
- [ARI API reference](artifact/references/reference.md)
- [Usage guide](artifact/使用说明.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI products](https://ari.funewa.com/zh/products)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and concise natural-language guidance with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid ARI operations can spend credits under the service confirmation and auto-confirm rules.]

## Skill Version(s):

1.4.8 (source: server release evidence, skill frontmatter, changelog, artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
