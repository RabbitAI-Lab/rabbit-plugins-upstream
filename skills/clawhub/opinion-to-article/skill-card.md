## Description:

从使用者自己的观点出发，AI 联网搜索拓展观点、重组逻辑层、绑定素材，产出带有个人 IP 标识的公众号文章或短视频脚本。面向自媒体创作者。触发词：写文章、做脚本、观点成文、把我的想法写成内容、opinion to article。

This skill is ready for commercial/non-commercial use.

## Publisher:

[shiyan521](https://clawhub.ai/user/shiyan521)

### License/Terms of Use:

MIT

## Use Case:

External self-media creators, bloggers, and content operators use this skill to turn their own viewpoint into a sourced public-account article or short-video script while preserving a personal expression style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses web search, so retrieved facts or examples may be incomplete, stale, or unsuitable for publication.

Mitigation: Require source labels for materials, mark unavailable claims as pending verification, and review facts before publishing.

Risk: Broad trigger phrases may activate this opinion-focused workflow when a generic writing assistant was intended.

Mitigation: Rename or narrow trigger phrases when the host skill system supports trigger customization.

Risk: Drafts may drift away from the user's intended viewpoint or personal style during restructuring.

Mitigation: Confirm the core viewpoint before drafting and incorporate user feedback into the expression preference card during revisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/shiyan521/skills/opinion-to-article)
- [README](artifact/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown article drafts or structured short-video scripts with source notes and feedback-driven revisions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include an expression preference card, sourced material library, outline, article draft, short-video script, and revision notes.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
