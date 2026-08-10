## Description:

Secure webhook token management using MGC Blackbox for DingTalk, WeCom, Feishu, Telegram, Slack, and similar notification targets while guiding agents toward token handling patterns that avoid exposing webhook secrets to the model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zkeviny](https://clawhub.ai/user/zkeviny)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure agents to send webhook notifications while keeping service tokens in MGC Blackbox rather than in prompts, logs, or generated code. It is suited for deployment alerts, monitoring notifications, CI/CD updates, and team collaboration bots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports that the skill is documentation-only but provides a concrete path that could retrieve stored webhook secrets despite zero-exposure claims.

Mitigation: Prefer the WebUI and mgc_run flow, avoid granting agents plaintext retrieval access, and review stored scripts before sealing or running them.

Risk: Webhook notification flows can disclose sensitive operational data if messages or bot permissions are too broad.

Mitigation: Use send-only or least-privilege webhook credentials, separate tokens per platform or bot, and rotate tokens regularly.

## Reference(s):

- [MGC Blackbox](https://github.com/zkeviny/MGC-Blackbox)
- [MGC Blackbox Issues](https://github.com/zkeviny/MGC-Blackbox/issues)
- [ClawHub Skill Page](https://clawhub.ai/zkeviny/skills/token-safe-webhook-sender)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON examples, shell commands, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces instructions for storing webhook tokens, invoking MGC tools, and passing runtime message content without exposing plaintext secrets to the model.]

## Skill Version(s):

1.2.0 (source: frontmatter, manifest, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
