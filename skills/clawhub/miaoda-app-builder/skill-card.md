## Description:

Create, modify, generate, and deploy websites, web apps, dashboards, SaaS products, internal tools, interactive web pages, Weixin mini programs, native iOS and Android mobile apps, and games on the Baidu Miaoda platform using natural-language instructions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seiriosplus](https://clawhub.ai/user/seiriosplus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create, modify, generate, and publish Miaoda-hosted applications or produce Miaoda task outputs from natural-language requests. It is suited for web products, dashboards, games, mobile apps, and document-style outputs when the user intends to work through a Miaoda account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act on the user's Miaoda account using MIAODA_API_KEY or a session-bound Miaoda proxy.

Mitigation: Install only in trusted agent environments, avoid exposing credentials in chat, logs, or shell history, and remove ambient session access when it is not needed.

Risk: The skill can generate and publish public apps on Miaoda.

Mitigation: Require explicit user confirmation before generation or publishing, then verify the returned status and public URL from the CLI output.

Risk: Workflow state is maintained by the Miaoda platform, so stale or missing app and conversation identifiers can affect the wrong project or create a new one.

Mitigation: Check app detail, conversation history, or trajectory output before continuing an existing project, and pass both appId and conversationId together for modifications.

## Reference(s):

- [Miaoda Official Website](https://www.miaoda.cn)
- [ClawHub Skill Page](https://clawhub.ai/seiriosplus/skills/miaoda-app-builder)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can initiate Miaoda account actions through CLI commands and may return application IDs, conversation IDs, status values, public URLs, or distribution links from the platform.]

## Skill Version(s):

1.0.13 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
