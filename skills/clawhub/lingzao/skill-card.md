## Description:

Lingzao helps WorkBuddy, OpenClaw, Codex, and similar agents route cross-platform creator research and self-media operations, with optional API-key access for public-content lookup, comments, video transcript extraction, WeChat article data, and creator image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[itxiaohao](https://clawhub.ai/user/itxiaohao)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, content operators, and agent users use Lingzao to plan, diagnose, rewrite, check, and review creator workflows across Xiaohongshu, Douyin, TikTok, Instagram, YouTube, WeChat Channels, and WeChat official accounts. With configured online access, it can support public-content research, comment review, transcript extraction, article data lookup, and creator image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online lookup and image generation can contact Lingzao services using a configured API key.

Mitigation: Install only when that online creator-research workflow is intended, configure the API key deliberately, and review the requested scope before approving expanded lookups or generation.

Risk: Selected reference images, screenshots, or private visual materials may be uploaded to Lingzao for the current generation request.

Mitigation: Do not provide sensitive or private images unless the user is comfortable with that upload; use per-run temporary paths and avoid storing reference images in the skill repository.

Risk: Broad routing can expand into more keywords, accounts, details, comments, transcripts, profile depth, or image counts than the user first requested.

Mitigation: Keep the first pass narrow and ask for confirmation before increasing the business scope of online research or generation.

Risk: Creator-operation advice and publishable copy may include unsupported claims, diversion language, or implied guarantees if not reviewed.

Mitigation: Apply the included platform-management and content-compliance gates before final Xiaohongshu-facing output, and avoid promises of viral growth, monetization, platform approval, or copying another creator's content.

## Reference(s):

- [Lingzao ClawHub skill listing](https://clawhub.ai/itxiaohao/skills/lingzao)
- [Lingzao dashboard and setup tutorials](https://lingzao.atian.vip)
- [Lingzao feature usage manual](https://my.feishu.cn/docx/Y2HQdj5mzoFx4vxfij3cl9TRnjh?from=from_copylink)
- [Artifact package index](artifact/index.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with inline shell commands, optional JSON command output, and locally saved generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Online lookup and image-generation commands require a configured Lingzao API key; generated images are saved to caller-provided local output paths.]

## Skill Version(s):

0.1.105 (source: server release metadata and artifact VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
