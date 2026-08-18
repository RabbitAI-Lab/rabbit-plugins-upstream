## Description:

Submit articles, shorts, and videos to ZARZOOM for multi-platform social posting, check submission status, pull analytics, and see which platforms each post will land on using customer-managed API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neildarrenltd](https://clawhub.ai/user/neildarrenltd)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit, validate, schedule, monitor, and analyze ZARZOOM social posts from OpenClaw. It helps users manage multi-platform publishing while surfacing compliance review status, platform eligibility, rate limits, and recovery guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Posting and calendar-edit actions can submit or alter content that may later publish across connected social accounts after ZARZOOM compliance review.

Mitigation: Confirm the content, schedule, and selected platforms before write actions, and use the narrowest ZARZOOM API key scopes needed for the task.

Risk: Exposure of the customer-managed ZARZOOM_API_KEY could allow unauthorized actions within that key's scopes.

Mitigation: Store the key only in private local configuration or environment variables, rotate it if exposed, and revoke stale or over-privileged keys.

Risk: Rate limits or failed media uploads can prevent submissions from completing as expected.

Mitigation: Surface rate-limit reset information to the user, avoid blind retries, and retry failed presigned upload flows with fresh upload keys.

## Reference(s):

- [ZARZOOM ClawHub Skill Page](https://clawhub.ai/neildarrenltd/skills/zarzoom)
- [ZARZOOM API Key Dashboard](https://zarzoom.com/dashboard/api-keys)
- [ZARZOOM API Endpoint Reference](artifact/reference/api-endpoints.md)
- [ZARZOOM API Error Codes](artifact/reference/error-codes.md)
- [ZARZOOM Worked Examples](artifact/reference/examples.md)
- [ZARZOOM OpenAPI Specification](https://zarzoom.com/api/v1/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with JSON request examples, shell commands, configuration snippets, and concise user-facing status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a customer-managed ZARZOOM_API_KEY; write actions require fresh idempotency keys and should confirm content, schedule, and target platforms before submission.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
