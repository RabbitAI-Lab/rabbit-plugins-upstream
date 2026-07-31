## Description: <br>
Detects abnormal body temperature rise or drop in livestock and poultry from thermal or visible-light imagery, and outputs fever/hypothermia early warnings based on visual thermal features. | 通过热成像或视觉特征识别畜禽体温异常，预警发热。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, farm operators, and animal-health teams use this skill to analyze livestock or poultry thermal and visible-light images or videos for early fever and hypothermia screening. It produces structured abnormal-temperature reports and can query cloud report history for the current internal identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Livestock images, videos, URLs, and analysis requests are sent to the configured Lifeemergence backend. <br>
Mitigation: Use the skill only for data you are permitted to submit to that backend, and avoid uploading unrelated sensitive material. <br>
Risk: The skill can silently create or reuse an internal identity and query cloud report history for that identity. <br>
Mitigation: Review workspace identity state before use in shared environments, and confirm that report history access matches the intended user or farm context. <br>
Risk: Authentication tokens may be stored in a local workspace SQLite database. <br>
Mitigation: Clear the workspace data database when retention is no longer needed, and keep the workspace access-controlled. <br>
Risk: The scanner guidance warns against placing unrelated secrets in data/smyx-api-key.txt. <br>
Mitigation: Keep data/smyx-api-key.txt limited to the expected internal identity value and do not reuse it as a general secret store. <br>
Risk: The skill provides screening output and does not provide veterinary diagnosis or treatment advice. <br>
Mitigation: Use outputs as early-warning support and confirm health decisions with professional veterinary and laboratory assessment. <br>


## Reference(s): <br>
- [Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-fever-detection-analysis) <br>
- [Publisher Profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [Livestock Fever Detection API Documentation](artifact/references/api_doc.md) <br>
- [Common Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown text with structured JSON analysis content and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save the analysis result to a user-selected output file.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter is 1.0.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
