## Description: <br>
Helps an agent prepare, publish, and summarize Markdown blog posts across CSDN, 51CTO, CNBlogs, and Juejin. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lainxxx](https://clawhub.ai/user/lainxxx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn article drafts or Markdown files into posts on one or more supported blogging platforms, then receive a per-platform success or failure summary. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses posting-account cookies and can publish publicly to configured blog accounts. <br>
Mitigation: Use it only with accounts you intend to publish from, confirm the exact destination platforms and draft or publish mode before execution, and avoid commands or outputs that reveal cookie values. <br>
Risk: The workflow retains ./temp/publish.md after publishing, which can leave sensitive or unpublished content on disk. <br>
Mitigation: Review the temporary file when needed, then delete ./temp/publish.md after publishing sensitive or unpublished material. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/lainXXX/blog-auto-poster-skill) <br>
- [ClawHub skill page](https://clawhub.ai/lainxxx/skills/blog-auto-poster-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands and publishing status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create a temporary ./temp/publish.md file for user review and publishes sequentially so one platform failure does not stop the others.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
