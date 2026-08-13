## Description:

灵造 helps WorkBuddy, OpenClaw, Codex, and similar agents route creator-operation workflows, prepare creator research, run public-content lookups when configured, and generate creator image assets after user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[itxiaohao](https://clawhub.ai/user/itxiaohao)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and agent users use Lingzao to plan, diagnose, rewrite, check, and review cross-platform self-media content workflows. When the user configures a Lingzao API key and confirms scope and credits, agents can also perform public-content research, comment or transcript extraction, WeChat article data checks, and creator image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send selected public links, prompts, and chosen reference images to the configured Lingzao service.

Mitigation: Install only if that data flow is acceptable, use a trusted base URL, and avoid sending sensitive material that is not needed for the task.

Risk: Public-data lookups and image generation can consume Lingzao credits.

Mitigation: Confirm task scope and likely credit use before paid actions, keep the first pass small, and require explicit confirmation before larger budgets.

Risk: Creator-content recommendations and generated drafts may be inaccurate, misleading, noncompliant, or unsuitable for publication.

Mitigation: Review outputs before publishing and apply the included platform management and compliance gates for Xiaohongshu-facing content.

Risk: Knowledge-base sync can place generated reports into user-selected external destinations.

Mitigation: Ask the user to choose the destination explicitly and keep credentials, temporary paths, and unnecessary sensitive details out of synced content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/itxiaohao/skills/lingzao)
- [Publisher Profile](https://clawhub.ai/user/itxiaohao)
- [Lingzao Dashboard](https://lingzao.atian.vip)
- [Lingzao Feature Manual](https://my.feishu.cn/docx/Y2HQdj5mzoFx4vxfij3cl9TRnjh?from=from_copylink)
- [Package Index](artifact/index.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON from CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid public-data lookups and image generation require a configured Lingzao API key, available credits, and user confirmation of scope and budget.]

## Skill Version(s):

0.1.101 (source: release.version, artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
