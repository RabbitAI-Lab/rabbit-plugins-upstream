## Description:

确认当前会话的登录入口身份，用于回答「你是哪个入口」「是不是同一个 AI 的另一个账号」「标记别搞错」这类问题

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to confirm the current session's entry identity, avoid confusing one login entry with another, and ask for user confirmation when the identity anchor cannot be resolved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad identity or verification wording.

Mitigation: Use it only for explicit entry or session identity checks.

Risk: Identity checks can become unreliable if the authority source is unclear or mutable.

Mitigation: Ensure any referenced authority configuration is clearly identified and read-only.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/identity-verify)
- [ClawHub publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Markdown or plain text response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May respond in Chinese by default or match the user's language.]

## Skill Version(s):

1.0.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
