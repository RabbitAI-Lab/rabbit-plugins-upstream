## Description: <br>
灵造 helps WorkBuddy, OpenClaw, Codex, and similar agents support creator research and self-media operations across Xiaohongshu, Douyin, TikTok, Instagram, YouTube, and WeChat public-account workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itxiaohao](https://clawhub.ai/user/itxiaohao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, marketers, and agent users use this skill to plan topics, diagnose accounts, design titles and covers, rewrite drafts, run pre-publish checks, review post-publish data, prepare cross-platform content packages, and call Lingzao public-data or image-generation services after confirming scope and credit use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public links, prompts, and selected reference images may be sent to the Lingzao service when paid lookup or image generation is used. <br>
Mitigation: Use the API key only for intended tasks, avoid private platform credentials or sensitive images, and confirm the scope before service calls. <br>
Risk: Paid public-data lookups, comment reads, transcript extraction, article metrics, and image generation can consume Lingzao credits. <br>
Mitigation: Keep credit-budget confirmations enabled, start with a small first-pass scope, and require explicit approval before larger plans. <br>
Risk: Knowledge-base export or local file output can persist generated analysis beyond the chat. <br>
Mitigation: Write or sync outputs only after the user intentionally selects the destination and confirms the export. <br>
Risk: A custom base URL or update command could route requests somewhere unexpected. <br>
Mitigation: Review the configured base URL and approve update or setup commands before running them. <br>


## Reference(s): <br>
- [Lingzao Skill page](https://clawhub.ai/itxiaohao/skills/lingzao) <br>
- [Lingzao dashboard and setup](https://lingzao.atian.vip) <br>
- [Lingzao feature usage manual](https://my.feishu.cn/docx/Y2HQdj5mzoFx4vxfij3cl9TRnjh?from=from_copylink) <br>
- [Package index](artifact/index.md) <br>
- [Main skill instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, code, text] <br>
**Output Format:** [Markdown, plain text, shell command examples, local files, and optional JSON from CLI commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require LINGZAO_API_KEY and confirmed credit use for public-data lookup, comments, transcript extraction, article metrics, or image generation.] <br>

## Skill Version(s): <br>
0.1.94 (source: evidence.release.version and artifact/VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
