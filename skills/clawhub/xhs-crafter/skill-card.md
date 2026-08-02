## Description: <br>
Xhs Crafter converts Markdown articles into 3:4 WeChat and Xiaohongshu image cards plus a compressed text draft through local HTML template assembly, validation, and Puppeteer screenshots, with optional external image search, AI image generation, and Feishu upload only after explicit consent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, social media operators, and agent users use this skill to turn an existing Markdown article into a local folder of polished 1080x1440 image cards and a short text draft for WeChat Official Account or Xiaohongshu publishing. It is intended for formatting and delivery workflows, not original writing, pure text layout, or video creation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional image search or AI image generation can send search terms or prompts to external services. <br>
Mitigation: Use these options only after separate explicit consent, and avoid sending sensitive, proprietary, or unpublished article details in search terms or prompts. <br>
Risk: Optional Feishu sync uploads generated PNG and text files to cloud storage. <br>
Mitigation: Keep delivery local unless the user accepts that the generated publishing materials will leave the local machine. <br>
Risk: Generated visual assets and compressed copy may misrepresent the source article if not reviewed. <br>
Mitigation: Review the generated PNG cards and text draft before publication, especially for quotes, data, claims, and image-source suitability. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/edwardwason/skills/xhs-crafter) <br>
- [README](artifact/README.md) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>
- [Workflow Reference](artifact/references/workflow.md) <br>
- [Image Sources Reference](artifact/references/image-sources.md) <br>
- [Layout Recipes](artifact/references/layout-recipes.md) <br>
- [Components Reference](artifact/references/components.md) <br>
- [Validation Script](artifact/assets/validate.js) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Local PNG image files and a UTF-8 text draft, with generated HTML and shell commands used during rendering and validation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default processing is local; optional image search, AI image generation, and Feishu upload require separate explicit user consent.] <br>

## Skill Version(s): <br>
7.8.0 (source: frontmatter, changelog, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
