## Description:

从智慧芽专利数据库查询专利的前向引用详情。当用户询问专利引用、被引用专利、引用文献、专利参考文献、前向引用、在先技术引用或想查看特定专利在申请过程中引用了哪些专利、非专利文献、patent cited references, forward citations, patent references, citation analysis, PatSnap时触发此技能。当用户提供专利ID或公开号并需要引用信息时，即使未明确说"前向引用"，任何关于专利引用了哪些参考文献的请求都适用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, IP professionals, and developers use this skill to query cited patent and non-patent literature for one or more patent IDs or publication numbers from the Zhihuiya patent database. It helps present returned citation data in grouped tables and summaries without fabricating records beyond the API response.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses patent query text, API credentials, session metadata, phone/SMS onboarding data, and generated response files with LinkFox services.

Mitigation: Install and run it only when LinkFox is trusted for those data types, keep API keys out of shared logs, and keep generated linkfox output directories out of source control or shared workspaces.

Risk: The bundled onboarding flow can create API keys and initiate billing or payment actions.

Mitigation: Run payment, order, or account commands only after the user explicitly requests them and confirms the plan and payment method.

Risk: The lookup consumes credits and cost scales with returned records.

Mitigation: Warn the user before running a query that may incur credits, avoid repeated speculative requests, and use the 24-hour cache for identical parameter combinations.

Risk: Endpoint environment variables can redirect requests away from the default LinkFox services.

Mitigation: Confirm endpoint variables point to official LinkFox services before sending credentials or patent query data.

## Reference(s):

- [智慧芽专利引用查询 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-patent-forward-citation)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [API Calls, Files, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance, shell commands, and JSON API responses or response summaries saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires patentId or patentNumber input, supports comma-separated batches up to 100 entries, uses API credentials, consumes LinkFox credits, caches identical requests for 24 hours, and writes full responses under the current working directory.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
