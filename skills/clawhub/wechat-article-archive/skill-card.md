## Description: <br>
Save WeChat Official Account articles and image-note / Xiaolushu pages from mp.weixin.qq.com into a user-specified local folder as Markdown plus local assets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[harven-droid](https://clawhub.ai/user/harven-droid) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to archive WeChat Official Account articles or image-note pages into a local folder as Markdown with copied image assets. It is suited for local preservation and review workflows, not cloud import or message sending. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches WeChat content and downloads referenced images from the network. <br>
Mitigation: Use it only for user-selected WeChat URLs or trusted saved HTML, and refresh dependencies from trusted registries. <br>
Risk: The skill writes Markdown and image files into a user-selected local directory. <br>
Mitigation: Use a dedicated output folder and review generated file paths and image failure reports before relying on the archive. <br>
Risk: A custom NODE path can change which runtime executes the bundled extractor. <br>
Mitigation: Avoid setting NODE unless the runtime path is trusted. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/harven-droid/skills/wechat-article-archive) <br>
- [Publisher Profile](https://clawhub.ai/user/harven-droid) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown files with local image assets and JSON execution summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or reuses a destination folder, writes an assets subdirectory, and reports paths, image counts, and image download failures.] <br>

## Skill Version(s): <br>
1.1.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
