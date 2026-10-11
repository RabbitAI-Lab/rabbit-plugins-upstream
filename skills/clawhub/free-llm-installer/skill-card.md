## Description:

Configures free LLM options for WorkBuddy and Claude Code, tests model capabilities, and monitors availability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT-0

## Use Case:

WorkBuddy and Claude Code users configure free or optional paid LLM providers, check model availability and capabilities, and receive guidance on maintaining their setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured providers can receive model requests, including sensitive prompts or images.

Mitigation: Do not send secrets, private code, customer data, screenshots, or production credentials through anonymous or free routes.

Risk: The optional Claude switcher can reroute Claude Code through a local proxy and retain request data in local logs.

Mitigation: Use the switcher only if you accept proxy routing and persistent logs; review Claude settings, proxy configuration, and failure logs after use.

Risk: Installing models changes local provider configuration and can enable paid services.

Mitigation: Install only when you intend to configure third-party providers; inspect WorkBuddy and Claude settings afterward and avoid paid routes unless intended.

## Reference(s):

- [Free LLM Installer on ClawHub](https://clawhub.ai/oracis/skills/free-llm-installer)
- [Zhipu AI open platform](https://open.bigmodel.cn)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text reports]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports live model checks and availability changes.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
