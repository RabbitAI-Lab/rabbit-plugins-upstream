## Description: <br>
将中文草稿整理为可对外发布的版本：清理创作标记、生成候选标题、简介与封面图，并输出独立的发布目录。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and publishing teams use this skill to turn a finished Chinese draft into a publication-ready local release with cleaned Markdown, candidate titles, a short summary, optional cover-image metadata, and versioned publish files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes local publication folders, release Markdown, metadata files, and article changelog entries. <br>
Mitigation: Review the target article path and proposed publish directory before allowing file-writing steps, and keep the original draft unchanged. <br>
Risk: Cover-image generation may be delegated to a separate wenqu-image workflow that can generate or upload image assets. <br>
Mitigation: Review the cover prompt and confirm any image-generation or upload step before accepting the final cover URL. <br>
Risk: The auto-publish document is a placeholder and does not implement platform publishing. <br>
Mitigation: Treat requests to publish to external platforms as unsupported unless a separate implemented and reviewed publishing workflow is present. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gogoingai/skills/wenqu-publish) <br>
- [Wenqu Publish Homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-publish) <br>
- [发布流程](references/workflow.md) <br>
- [标题与简介写作规范](references/title-summary.md) <br>
- [封面图画图提示规范](references/cover-prompt.md) <br>
- [自动发布扩展点](references/auto-publish.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Guidance, Configuration] <br>
**Output Format:** [Markdown files and structured publication metadata] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates versioned local publish directories, release Markdown, metadata files, and changelog entries; optional cover-image output depends on the separate wenqu-image workflow.] <br>

## Skill Version(s): <br>
0.1.17 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
