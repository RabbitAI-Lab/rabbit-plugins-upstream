## Description: <br>
Publishes Markdown to a public URL and returns the link. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuvadm](https://clawhub.ai/user/yuvadm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to publish selected Markdown files or generated Markdown pages to a shareable public URL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill publishes selected Markdown to a public, unauthenticated external service where pages are public and cannot be edited after publishing. <br>
Mitigation: Review content for secrets, private conversation details, personal data, and proprietary material before publication. <br>
Risk: A mistaken or outdated publication cannot be changed in place. <br>
Mitigation: Publish a corrected replacement page and use the service's report link when removal is needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yuvadm/skills/markdown-publish) <br>
- [markdown.page agent guide](https://markdown.page/llms.txt) <br>
- [markdown.page API reference](https://markdown.page/api.md) <br>
- [markdown.page FAQ](https://markdown.page/faq.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with an inline bash command and a returned public URL] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Successful publication returns a https://markdown.page/... URL; raw Markdown is available by appending .md.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
