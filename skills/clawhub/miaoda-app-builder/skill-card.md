## Description:

Create, modify, generate, and deploy websites, web apps, dashboards, SaaS products, internal tools, interactive web pages, Weixin mini programs, native iOS and Android mobile apps, and games on the Baidu Miaoda platform using natural-language instructions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seiriosplus](https://clawhub.ai/user/seiriosplus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create, iterate, publish, and download Miaoda-hosted applications and content artifacts through a packaged CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, modify, publish, and download remote Miaoda projects using the user's account or session.

Mitigation: Confirm intent before generation, publishing, or downloads, and review app details or trajectory before state-changing commands.

Risk: MIAODA_API_KEY and conversation identifiers can grant access to account projects or sensitive project history.

Mitigation: Keep keys out of shared files, rotate exposed keys, and treat appId and conversationId values as sensitive.

Risk: Broad prompts can trigger costly or unintended Miaoda operations because the skill has weak scoping and consent controls.

Mitigation: Require explicit approval before broad app-building prompts, production publishing, or downloading generated artifacts.

## Reference(s):

- [Miaoda official website](https://www.miaoda.cn)
- [ClawHub skill page](https://clawhub.ai/seiriosplus/skills/miaoda-app-builder)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses; generated artifacts may be source ZIPs or task files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and MIAODA_API_KEY or a supported session-bound proxy; can create, modify, publish, and download remote Miaoda projects.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
