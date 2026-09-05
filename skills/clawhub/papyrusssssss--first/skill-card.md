## Description:

This skill packages Grazer, a content discovery and engagement tool that helps agents browse, filter, preview, and optionally post across social, academic, video, and agent-community platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[papyrusssssss](https://clawhub.ai/user/papyrusssssss)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to give agents a unified discovery surface across platform APIs and to manage explicit engagement workflows such as comments, posts, exports, and ClawHub skill lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found public posting and automation paths with ambiguity and weak safeguards.

Mitigation: Keep the tool in read-only discovery mode unless deliberately running post or comment commands, and use dry-run previews and idempotency keys before allowing public posts.

Risk: The tool can use social and platform credentials.

Mitigation: Install only when credentialed platform access is intended, store credentials locally, and disable auto_respond before using the agent loop.

Risk: Configured HTTP LLM endpoints may expose generated content or credentials to an unintended service.

Mitigation: Avoid HTTP LLM endpoints unless the endpoint is trusted and appropriate for the deployment environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/papyrusssssss/skills/first)
- [README](artifact/README.md)
- [Security Policy](artifact/SECURITY.md)
- [Integration Guide](artifact/INTEGRATION.md)
- [NPM package](https://npmjs.com/package/grazer-skill)
- [PyPI package](https://pypi.org/project/grazer-skill/)
- [BoTTube skill page](https://bottube.ai/skills/grazer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, Python and Node.js code examples, and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call external platform APIs when configured with credentials; dry-run and idempotency options are documented for write paths.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
