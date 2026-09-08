## Description:

Vimeo API integration with managed OAuth for uploading, managing, and organizing videos, showcases, folders, likes, watch-later items, comments, followers, channels, and categories through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect a Vimeo account through Maton, inspect account and video resources, and perform approved Vimeo management actions such as organizing videos, folders, showcases, comments, likes, and follows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify resources in a connected Vimeo account through Maton.

Mitigation: Use OAuth when possible, connect only the intended account, choose the narrowest available scopes, and require explicit confirmation before any write, delete, comment, follow, or sharing-related operation.

Risk: Ambiguous account or connection selection could apply an action to the wrong Vimeo account.

Mitigation: Specify the intended Maton profile and Vimeo connection when multiple accounts or connections are available.

Risk: Long-lived API keys can leak through environment variables, logs, command history, or pasted output when the CLI is unavailable.

Mitigation: Prefer OAuth and the Maton CLI credential store; when raw HTTP is necessary, keep the API key only in the process environment, never print it, and send it only to api.maton.ai.

## Reference(s):

- [Vimeo API Reference](https://developer.vimeo.com/api/reference)
- [Vimeo Developer Portal](https://developer.vimeo.com)
- [Vimeo API Authentication](https://developer.vimeo.com/api/authentication)
- [Vimeo Upload API](https://developer.vimeo.com/api/upload/videos)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an approved Vimeo connection; write operations require explicit user confirmation.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
