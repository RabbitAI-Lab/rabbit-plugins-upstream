## Description:

通过专利ID或公开号查询智慧芽（PatSnap）的专利家族信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve factual patent family members and equivalents from Zhihuiya (PatSnap) by patent ID or publication number. It supports Simple Family, INPADOC Family, and PatSnap Family lookup, including batch requests up to 100 patents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles patent queries, API keys, phone-number login, SMS verification, billing, and payment flows.

Mitigation: Use it only when the LinkFox and PatSnap workflow is trusted; prefer obtaining an API key directly, avoid sharing phone numbers or SMS codes with the agent unless necessary, and confirm billing actions before purchase or lookup.

Risk: Gateway and account endpoints can be redirected through environment variables.

Mitigation: Verify gateway and account environment variables point to official LinkFox domains before running account, billing, or patent lookup commands.

Risk: Patent queries, feedback, and response data may be transmitted to third-party services and persisted in local JSON files.

Mitigation: Avoid sending confidential patent research or sensitive feedback unless that transmission and storage are intended; review generated JSON files before sharing them.

Risk: Patent family lookups consume credits and may become costly for batch requests or repeated attempts.

Mitigation: Warn users about credit consumption before making calls, rely on the built-in cache for duplicate requests, and ask for confirmation before additional billable lookups.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-patent-family)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [智慧芽专利家族查询 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API call instructions, shell commands, and JSON response files or summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The lookup script persists full JSON responses under a linkfox session data directory, prints full JSON for small responses, and prints a compact summary for larger responses unless --inline is used.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
