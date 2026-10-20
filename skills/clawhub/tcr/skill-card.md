## Description:

Helps run OpenClaw through a local tcr proxy that pools the user's Claude and ChatGPT subscriptions, checks account availability, and verifies routed turns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dhkts1](https://clawhub.ai/user/dhkts1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers running OpenClaw on their own machines use this skill to configure Claude and ChatGPT subscription pooling through tcr, start the Gateway, and check that model requests reach the pool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local proxy can decrypt pooled Claude and ChatGPT prompts and replies.

Mitigation: Use it only for accounts and traffic you trust the local proxy to handle; review its access before starting the Gateway.

Risk: The proxy stores local account tokens and usage metadata, and the launcher routes the whole OpenClaw process through it.

Mitigation: Protect local account files and confirm the scope of process-wide routing before enabling the launcher.

Risk: A release checksum does not establish authenticity when the release is unsigned.

Mitigation: Verify the GitHub release independently before installing it.

## Reference(s):

- [tcr installation and documentation](https://github.com/dhkts1/tcr)
- [OpenClaw integration guide](https://github.com/dhkts1/tcr/blob/main/docs/openclaw.md)
- [tcr release downloads](https://github.com/dhkts1/tcr/releases/latest)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes steps to check pool availability and confirm routed Claude and ChatGPT turns.]

## Skill Version(s):

0.1.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
