## Description: <br>
Analyzes writing samples to extract reusable style fingerprints, recommend writing formulas, and generate new content in a similar style. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, marketers, and writing assistants use this skill to distill an author's style from supplied samples, store a structured style fingerprint, and draft new text that follows the saved fingerprint and selected writing formula. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed to mimic writing styles, which can be misused to impersonate an author or obscure generated content. <br>
Mitigation: Use it only with your own writing or with permission, and label generated content appropriately. <br>
Risk: Saved style fingerprints remain on disk under style_fingerprints/{author_id}.json until removed or overwritten. <br>
Mitigation: Review stored fingerprint files, avoid saving sensitive samples, and delete or overwrite fingerprints that are no longer needed. <br>
Risk: Documentation inconsistencies may make storage behavior or cloning boundaries unclear to users. <br>
Mitigation: Review the skill documentation before use and verify expected distill, save, and preview behavior in a controlled workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-writing-style-cloner) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON responses and Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save per-author style fingerprint JSON files under style_fingerprints/{author_id}.json when the save workflow is used.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
