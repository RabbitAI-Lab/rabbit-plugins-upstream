## Description:

Queries Zhihuiya (PatSnap) patent forward-citation data, including citation counts and details about citing patents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, patent analysts, and developers use this skill to look up forward-citation metrics for one or more patents by Zhihuiya patent ID or publication number. It helps compare citation counts, family citation counts, and citing patent details without providing patent valuation or investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent identifiers and citation responses are handled by LinkFox and saved locally during use.

Mitigation: Submit only patent identifiers appropriate for LinkFox handling, and review or remove saved response files when they contain sensitive matter.

Risk: Authentication or billing recovery can involve phone verification, API key issuance, plan purchase, and payment status flows.

Mitigation: Prefer LinkFox self-service signup or billing, share SMS codes only when intentionally creating or accessing a LinkFox account, and verify any selected plan or payment method before proceeding.

Risk: Generated API keys and cached response files may expose account access or query history if shared or committed.

Mitigation: Store keys in environment variables, avoid committing LinkFox output or cache directories, and rotate keys if exposure is suspected.

Risk: The skill includes automatic feedback-sharing behavior.

Mitigation: Review feedback content before sending when possible, especially if it may include user intent, patent identifiers, or operational context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-patent-cited)
- [智慧芽-专利被引用 API 参考](artifact/references/api.md)
- [解决认证和积分问题](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with JSON request parameters, shell commands, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts patentId or patentNumber values, caches repeated queries for 24 hours, and writes full API responses under a LinkFox session data directory.]

## Skill Version(s):

1.0.8 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
