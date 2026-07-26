## Description: <br>
Accurately identifies cat and dog breeds and supports distinguishing between different individuals in multi-pet households; an essential assistant for intelligent pet butlers. | 宠物品种个体识别技能，精准识别猫狗宠物品种，支持多宠家庭区分不同独立个体，智能宠物管家好帮手 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to analyze pet images or videos, identify cat and dog breeds, distinguish individual pets in multi-pet households, and retrieve prior recognition reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Media and URL inputs are sent to a cloud pet-recognition service. <br>
Mitigation: Use only media acceptable for external cloud processing, and avoid private household footage or identifying content unless the account linkage and provider retention model are acceptable. <br>
Risk: The skill silently creates or reuses an account identity and stores authentication tokens/profile data in the workspace. <br>
Mitigation: Review the workspace data and account-linkage behavior before installation; use an isolated workspace or account when privacy boundaries matter. <br>
Risk: History and report APIs can retrieve prior recognition reports tied to the managed identity. <br>
Mitigation: Limit access to the workspace and provider account, and avoid shared identities for sensitive media. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-breed-individual-recognition-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API 接口文档](artifact/references/api_doc.md) <br>
- [smyx_analysis API接口文档](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files] <br>
**Output Format:** [Markdown or JSON analysis report text, with optional file output when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include pet count, breed and individual labels, confidence values, remarks, history entries, and report/export links.] <br>

## Skill Version(s): <br>
1.0.8 (source: SKILL.md frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
