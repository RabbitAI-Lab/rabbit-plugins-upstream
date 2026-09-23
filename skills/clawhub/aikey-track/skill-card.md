## Description:

AI KEY·有什么到期了 tracks commitments, expiry dates, watch items, in-flight diagnoses, and publish queues across sessions, then surfaces due items without re-litigating the original trigger conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to preserve future check points such as commitments, expirations, watch items, partially completed diagnoses, and publish queues, then review what is due at the right time. It is especially suited for reminders that need original conditions, rationale, and prior rejected options preserved across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent tracking and memory files may retain sensitive customer names, amounts, or business details for a long time.

Mitigation: Confirm the configured tracking and memory folders before use, and store sensitive subjects with codes or redacted descriptions instead of raw details.

Risk: Ordinary reminder phrases may trigger the skill when the user intended a one-off response rather than persistent tracking.

Mitigation: Use explicit invocations for intentional tracking and decline to record items that lack a date, a clear future review need, or an acceptable storage location.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/aikey-track)
- [AI KEY README upgrade notes](https://github.com/iamzifei/aikey#老用户升级zmm-已改名为-ai-key)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with YAML frontmatter examples and concise status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local tracking records, due-item summaries, continuation context, and reminder handling guidance; it does not execute the user's due actions.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
