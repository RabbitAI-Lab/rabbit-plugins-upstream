## Description:

灵造 helps WorkBuddy, OpenClaw, Codex, and similar agents route cross-platform creator research and self-media operations work, with optional paid public-content lookup, comment analysis, transcript extraction, WeChat article data, and creator image generation when the user configures Lingzao credits and an API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[itxiaohao](https://clawhub.ai/user/itxiaohao)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, creator-operations teams, and agent users use this skill to plan topics, analyze accounts and public content, design titles and covers, check pre-publication risk, review post-publication data, package cross-platform content, and optionally call Lingzao paid services for public lookup or image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend paid Lingzao credits for public-content lookup, comment retrieval, transcript extraction, article data, and image generation.

Mitigation: Confirm task scope and estimated credit use before paid calls, keep the first pass small, and require explicit user confirmation before larger plans.

Risk: The skill stores a Lingzao API key and base URL in local configuration when setup is run.

Mitigation: Review the API key and base URL before setup, rely on the masked config display for checks, and avoid exposing credentials in user-facing output.

Risk: User-provided screenshots, reference images, links, or content may be used in the current Lingzao request.

Mitigation: Avoid sending private screenshots, credentials, cookies, or sensitive reference images unless the user intends them to be used for that request.

Risk: Creator-operation guidance can become misleading if it promises outcomes or copies another creator too closely.

Mitigation: Keep outputs framed as workflow support, avoid promises of viral growth or monetization, and use the included platform and content risk gates for publishable Xiaohongshu content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/itxiaohao/skills/lingzao)
- [Lingzao Dashboard and Setup Hub](https://lingzao.atian.vip)
- [Lingzao Usage Manual](https://my.feishu.cn/docx/Y2HQdj5mzoFx4vxfij3cl9TRnjh?from=from_copylink)
- [Package Index](artifact/index.md)
- [Router Index](artifact/playbooks/router-index.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with optional shell commands, configuration JSON, generated files, and saved image assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid public-content lookups and image generation require user-confirmed scope, credit budget, and a configured Lingzao API key.]

## Skill Version(s):

0.1.100 (source: server release evidence and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
