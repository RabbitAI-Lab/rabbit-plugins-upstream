## Description:

Helps developers build, debug, scaffold, and publish WeChat Mini Programs, including project structure, Canvas 2D, common runtime errors, AppID setup, experience-member permissions, and upload/review/release workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haohao642](https://clawhub.ai/user/haohao642)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create runnable WeChat Mini Program projects, diagnose common Mini Program issues, and prepare projects for preview, review, and release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled scaffolder can overwrite existing WeChat Mini Program files when run with --force or after overwrite confirmation.

Mitigation: Run it in a new or clearly intended project directory, review the listed scaffold files before proceeding, and avoid --force unless overwriting is intentional.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haohao642/skills/wb-skill-wechat-miniprogram-helper-skill)
- [Server-resolved GitHub provenance](https://github.com/haohao642/wb-skill-wechat-miniprogram-helper-skill)
- [Publisher profile](https://clawhub.ai/user/haohao642)
- [WeChat Mini Program architecture and basics](references/architecture-and-basics.md)
- [WeChat Mini Program common pitfalls](references/common-pitfalls.md)
- [WeChat Mini Program publishing](references/publishing.md)
- [WeChat sitemap documentation](https://developers.weixin.qq.com/miniprogram/dev/framework/sitemap.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code, shell commands, and generated project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create WeChat Mini Program scaffold files when the bundled scaffolder is invoked.]

## Skill Version(s):

0.1.1 (source: server release metadata; artifact frontmatter says 0.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
