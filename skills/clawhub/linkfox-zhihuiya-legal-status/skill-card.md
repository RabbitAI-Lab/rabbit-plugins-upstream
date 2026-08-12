## Description:

Queries the Zhihuiya (PatSnap) database for patent legal status, validity, and legal-event history by patent ID or publication number.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and patent professionals use this skill to check whether patents are active, inactive, pending, expired, revoked, or otherwise affected by legal events such as transfer, license, pledge, litigation, opposition, or re-examination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent identifiers and feedback content may be sent to LinkFox services.

Mitigation: Confirm the user is comfortable sharing the identifiers and avoid submitting confidential patent data unless the environment and account terms allow it.

Risk: API keys may be read from environment variables or generated during onboarding.

Mitigation: Treat generated keys as secrets, store them only in approved environment variables, and avoid printing or pasting them into shared logs.

Risk: The onboarding flow can initiate paid plan orders after a user selects a plan and payment method.

Mitigation: Show available plans, payment method, and cost before ordering, and proceed only after explicit user confirmation.

Risk: Full API responses are persistently saved in local LinkFox session data and may contain sensitive patent lookup results.

Mitigation: Protect or clean up saved response and cache files according to the workspace's data-handling requirements.

Risk: Endpoint environment variables can redirect requests to alternate LinkFox-compatible services.

Mitigation: Verify LINKFOX_* endpoint variables before use, especially in shared or production environments.

## Reference(s):

- [智慧芽专利法律状态查询 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON files, guidance]

**Output Format:** [Markdown guidance with shell commands; API responses as JSON printed to stdout and saved to local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Caches identical requests for 24 hours; saves full responses under a LinkFox session data directory; summarizes responses over 8 KB unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
