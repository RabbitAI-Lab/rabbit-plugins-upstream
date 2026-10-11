## Description:

Uses the dLazy Kimi K3 service for complex analysis, coding, and writing with text, image, and video understanding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can request long-form analysis, coding help, and writing from the hosted Kimi K3 model, optionally supplying images or videos for understanding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media may be sent to dLazy's hosted service.

Mitigation: Do not submit sensitive prompts or media without approval for external processing.

Risk: Signing in or setting an API key stores credentials in local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke keys if exposed.

Risk: Installation relies on an external npm CLI.

Mitigation: Review the upstream CLI before installing if stronger supply-chain assurance is needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI homepage (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Plain text or Markdown, including code when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns a structured JSON result; asynchronous calls may return a task ID before the result is ready.]

## Skill Version(s):

1.2.22 (source: server-resolved ClawHub release; artifact frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
