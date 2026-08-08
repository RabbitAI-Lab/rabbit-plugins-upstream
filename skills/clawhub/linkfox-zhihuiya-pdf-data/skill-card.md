## Description:

通过专利ID或公开号从智慧芽专利数据库下载专利PDF全文文档。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve patent PDF full-text download links from the Zhihuiya/PatSnap patent database by patent ID or publication number, including batch retrieval and optional family-patent substitution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles account login, API-key generation, payment flows, and feedback reporting in addition to PDF retrieval.

Mitigation: Install it only for intended LinkFox/Zhihuiya paid-service use, review account and payment steps before execution, and protect API keys, phone verification codes, payment details, and feedback content.

Risk: The skill persists full API responses, session metadata, and cache files that may contain patent queries, result data, and download links.

Mitigation: Run it from a workspace appropriate for sensitive data, avoid full inline output unless needed, and remove generated linkfox data and cache files when they are no longer required.

Risk: Patent PDF requests can consume paid credits, and batch requests may multiply cost.

Mitigation: Confirm patent identifiers, result count expectations, and family-substitution settings before making calls; avoid automatic retries or speculative repeated queries.

## Reference(s):

- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-pdf-data)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown tables or lists with patent PDF links; JSON for saved API responses and command outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save full API responses, session metadata, and 24-hour cache files under a local linkfox directory.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
