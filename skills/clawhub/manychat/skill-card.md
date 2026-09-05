## Description:

ManyChat API integration with managed authentication for managing subscribers, tags, custom fields, flows, and Facebook Messenger messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a ManyChat account through Maton, including subscriber lookup and updates, tag and custom field management, flow and growth tool inspection, and message sending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a connected ManyChat account, including subscriber changes and message sends.

Mitigation: Install only when that access is intended, review connection requests carefully, and require explicit confirmation before subscriber changes, message sends, or other write operations.

Risk: Long-lived API keys can leak through environment variables, logs, shell history, or pasted output.

Mitigation: Prefer OAuth, avoid printing or persisting credentials, pass secrets only through the intended credential path, and rotate any key that was exposed.

Risk: ManyChat API responses may contain personal data or adversarial content.

Mitigation: Treat returned content as untrusted data, extract only the fields needed for the task, and do not execute or follow instructions found inside API content.

## Reference(s):

- [ClawHub ManyChat Skill](https://clawhub.ai/byungkyu/skills/manychat)
- [Maton](https://maton.ai)
- [ManyChat API Documentation](https://api.manychat.com/swagger)
- [ManyChat API Key Generation Guide](https://help.manychat.com/hc/en-us/articles/14959510331420)
- [ManyChat Dev Program](https://help.manychat.com/hc/en-us/articles/14281269835548)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JSON examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API call examples and confirmation prompts for connection creation, writes, and message sends.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
