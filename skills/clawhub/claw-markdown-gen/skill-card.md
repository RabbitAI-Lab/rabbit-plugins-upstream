## Description: <br>
Generates platform-styled Markdown articles from webpage text and image metadata for WeChat, Zhihu, Juejin, Xiaohongshu, and Toutiao publishing workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[webkixi](https://clawhub.ai/user/webkixi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, marketers, and developers use this skill through the ClawMarkDown browser plugin to turn webpage articles into polished Chinese Markdown posts with platform-specific style, rewrite depth, word-count control, and image placement metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected webpage text, image metadata, and AI image prompts may be sent to configured AI services or an optional image-generation API. <br>
Mitigation: Avoid private account pages, secrets, internal documents, and confidential customer content; review the configured AI services before use. <br>
Risk: Generated Markdown may include SVG or Mermaid content in heavy rewrite mode, and downstream renderers may treat that content as active. <br>
Mitigation: Sanitize SVG and Mermaid output before rendering or publishing it in systems that allow active content. <br>
Risk: AI rewriting can change emphasis or introduce factual drift in publishable articles. <br>
Mitigation: Review the generated Markdown against the source article before publishing or copying it into platform editors. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/webkixi/skills/claw-markdown-gen) <br>
- [Image handling reference](references/image-handling.md) <br>
- [Humanized Chinese rewriting reference](references/ren-zh.md) <br>
- [WeChat style configuration](references/styles/wechat_common_style.json) <br>
- [Zhihu style configuration](references/styles/zhihu_common_style.json) <br>
- [Juejin style configuration](references/styles/juejin_common_style.json) <br>
- [Xiaohongshu style configuration](references/styles/xiaohongshu_common_style.json) <br>
- [Toutiao style configuration](references/styles/toutiao_common_style.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code] <br>
**Output Format:** [Markdown article with image placeholders, keyword comments, and optional SVG or Mermaid code blocks.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Target word count, rewrite depth, platform style, and image metadata shape the generated article; heavy rewrite mode may replace AI image placeholders with generated image links.] <br>

## Skill Version(s): <br>
2.3.1 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
