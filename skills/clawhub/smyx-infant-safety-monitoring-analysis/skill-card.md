## Description: <br>
Monitors infant behavior from image or video inputs with visual AI, identifying risks such as mouth or nose obstruction, climbing, crib escape, or falling from bed, and returns safety warnings and care suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and caregivers can use this skill through an agent to analyze infant activity media, surface high-risk behavior indicators, and generate safety-monitoring reports. The results are assistive safety guidance and do not replace real-time caregiver supervision or professional care. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive infant or household media and metadata may be sent to the publisher's cloud service. <br>
Mitigation: Use only media you are authorized to process and avoid real infant or household footage unless cloud processing by the publisher is acceptable. <br>
Risk: The skill creates and reuses local account/session state and can retrieve cloud-linked history reports. <br>
Mitigation: Review local identity and session handling before installation, and avoid the history feature unless cloud-linked report retrieval is intended. <br>
Risk: The safety analysis may be incomplete or inaccurate and should not be treated as professional care advice. <br>
Mitigation: Treat outputs as assistive alerts and care suggestions only; maintain real-time caregiver supervision and review any warnings before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-safety-monitoring-analysis) <br>
- [婴儿智能安全看护分析 API 文档](artifact/references/api_doc.md) <br>
- [API接口文档](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON safety analysis report with optional report link] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud-linked historical report listings and report export URLs.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata; artifact frontmatter says 1.0.14) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
