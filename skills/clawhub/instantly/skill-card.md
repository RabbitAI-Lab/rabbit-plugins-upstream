## Description:

Instantly API integration with managed OAuth for managing cold email campaigns, leads, sending accounts, emails, and analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an Instantly account through Maton and guide agents through campaign, lead, account, email, analytics, and related API workflows. It emphasizes read/list calls first and explicit user confirmation before new connections, writes, sends, or deletions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on a connected Instantly account, including creating campaigns, adding leads, changing sending accounts, replying or forwarding emails, and deleting records.

Mitigation: Use OAuth where possible, connect only the needed account, specify the intended connection when multiple accounts exist, and require explicit confirmation before any write, send, or delete action.

Risk: Long-lived API keys or provider-issued tokens could be exposed through command lines, logs, files, or copied output.

Mitigation: Prefer OAuth and the Maton CLI credential store; when an API key is unavoidable, read it from the process environment, never print or persist it, and rotate it if exposed.

Risk: Campaign, lead, email, and webhook content returned by the API may contain untrusted or adversarial text.

Mitigation: Treat fetched content as data, do not execute or follow instructions from it, and pass external values as discrete arguments rather than interpolating them into shell commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/instantly)
- [Maton Homepage](https://maton.ai)
- [Instantly API V2 Documentation](https://developer.instantly.ai/api-reference)
- [Instantly API Introduction](https://developer.instantly.ai/)
- [Instantly Help Center](https://help.instantly.ai/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, API calls]

**Output Format:** [Markdown with inline shell, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user confirmation before connection creation or data-changing operations.]

## Skill Version(s):

1.2.2 (source: ClawHub release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
