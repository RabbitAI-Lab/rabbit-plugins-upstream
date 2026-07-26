## Description: <br>
Monitors infant images or videos with visual AI to identify high-risk behaviors such as rolling over, mouth/nose obstruction, climbing, fence crossing, and fall risks, then returns safety warnings and care suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, parents, and developers use this skill to analyze infant image or video inputs for safety hazards and retrieve structured reports or historical report lists. Results are advisory and do not replace real-time human supervision or professional care. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive infant image or video inputs and sends inputs or URLs to a cloud service. <br>
Mitigation: Install only when the publisher is trusted, obtain appropriate consent for child media, and avoid submitting unnecessary or highly sensitive footage. <br>
Risk: The skill can silently create or reuse an internal identity and store returned service tokens locally. <br>
Mitigation: Review account linkage and token storage before deployment, restrict execution to trusted environments, and clear local credentials when access should end. <br>
Risk: The skill can query cloud-stored historical reports. <br>
Mitigation: Confirm that cloud retention, access control, and report-sharing behavior match the deployment's privacy expectations. <br>


## Reference(s): <br>
- [婴儿智能安全看护分析 API 文档](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-safety-monitoring-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown safety report or structured JSON, with optional report links and saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call cloud APIs for analysis and historical report retrieval.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter says 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
