## Description: <br>
Identifies obesity, emaciation, external injuries, skin abnormalities, and abnormal mental states, helping pet owners detect health issues promptly. | 宠物体态健康分析技能，识别肥胖、消瘦、外伤、皮肤异常、精神状态异常，帮助宠物主人及时发现宠物健康问题 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent developers use this skill to analyze pet images or videos for body-condition, skin, injury, and mental-state signals, then receive a structured report with suggested next steps. Results are health references and should not replace professional veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads pet photos, videos, or media URLs to a lifeemergence cloud service for analysis. <br>
Mitigation: Install only when cloud processing of the media is acceptable, and avoid submitting sensitive media unless the deployment policy permits it. <br>
Risk: The skill silently manages local and remote identity tokens to associate reports with an internal identity. <br>
Mitigation: Review or clear workspace data/smyx-api-key.txt and the workspace data SQLite database when identity reuse or token persistence is not desired. <br>
Risk: Health analysis output may be mistaken for a professional veterinary diagnosis. <br>
Mitigation: Present results as health reference information and direct users to seek veterinary care for abnormal findings or urgent concerns. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-body-health-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON reports with command-line examples and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports basic, standard, and JSON detail levels for single media analysis or historical report listing.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
