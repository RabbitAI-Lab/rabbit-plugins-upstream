## Description: <br>
Monitors infant behavior via visual AI, identifying high-risk actions such as rolling over, mouth or nose obstruction, climbing, crib or bed escape, and fall risk, then returning safety warnings and care suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and caregivers use this agent skill to analyze infant activity videos or image/video URLs for safety risks and to retrieve cloud-hosted historical safety reports. The output is an assistive safety report and does not replace real-time supervision or professional care. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Infant or home media may be uploaded to configured LifeEmergence cloud services for analysis. <br>
Mitigation: Use only with explicit user consent for remote processing of sensitive media, and prefer deployments that document retention, deletion, and access controls. <br>
Risk: The skill can silently create or reuse a local identity and retrieve account-linked report history. <br>
Mitigation: Review identity and token handling before deployment, disclose account association to users, and provide controls for clearing local credentials and report history. <br>
Risk: Safety outputs may be mistaken for professional care or a substitute for real-time supervision. <br>
Mitigation: Present outputs as assistive warnings and recommendations only, and retain clear human supervision requirements in user-facing workflows. <br>


## Reference(s): <br>
- [婴儿智能安全看护分析 API 文档](references/api_doc.md) <br>
- [API接口文档](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON safety analysis report with warning text, care suggestions, history tables, report links, and optional saved output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports basic, standard, and json detail modes; accepts local media paths or public media URLs; historical report queries return account-linked cloud data.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata; artifact frontmatter states 1.0.14) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
