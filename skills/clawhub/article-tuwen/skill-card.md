## Description: <br>
Article Tuwen converts provided URLs, files, or text into a long-form article enriched with web search, 5-9 social cards, and a text summary, while creating local files and keeping cloud sync opt-in. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and content operators use this skill to turn supplied source material into publishable social-card assets with an accompanying article and summary. It is intended for explicit material-to-card conversion workflows, not original writing, video production, or plain-text formatting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic web fetching, web searching, and external image downloads may expose source URLs or retrieve untrusted media during conversion. <br>
Mitigation: Invoke the skill only with material suitable for network-assisted processing, and avoid confidential inputs unless that network behavior is acceptable. <br>
Risk: Generated articles, cards, and summaries may contain sensitive information derived from the user's source material. <br>
Mitigation: Review generated outputs before sharing them and approve Feishu sync only when the generated files are safe to upload. <br>
Risk: The workflow invokes sub-skills and creates files on the Desktop after the user triggers the conversion. <br>
Mitigation: Install and use the required sub-skills only in a trusted agent environment, and inspect the created output folder before publication. <br>


## Reference(s): <br>
- [Article Tuwen on ClawHub](https://clawhub.ai/edwardwason/skills/article-tuwen) <br>
- [Article Tuwen Pipeline](artifact/references/pipeline.md) <br>
- [lark-cli](https://github.com/larksuite/lark-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, shell commands, configuration] <br>
**Output Format:** [Local PNG images, Markdown article, text summary, image-source JSON, and optional Feishu link] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates 5-9 1080x1440 PNG cards, a 2500-4000 word article, an 800-1000 character text summary, and used-images.json; Feishu upload requires explicit user confirmation.] <br>

## Skill Version(s): <br>
1.1.2 (source: frontmatter, changelog, server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
