## Description: <br>
Aquarium Plant Health Monitor analyzes aquarium plant images or video to detect visual signs such as yellowing, bleaching, blackening, melting, curling, holes, algae, and nutrient-deficiency symptoms, then returns a structured health assessment and care guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External aquarium hobbyists, aquascaping shops, and developers can use the skill to submit aquarium plant media for cloud analysis, review structured health findings, and retrieve historical reports. The skill supports visual monitoring workflows for smart aquariums, aquascaping tanks, and aquarium shops. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Aquarium media and report queries are sent to the publisher's cloud service. <br>
Mitigation: Use the skill only with media and report data that are acceptable to share with the publisher-operated service. <br>
Risk: The skill silently creates or reuses a local account identity and stores service tokens in the workspace data area. <br>
Mitigation: Review workspace identity and token storage before installation, and avoid shared or sensitive workspaces where automatic identity reuse is not acceptable. <br>
Risk: Historical report queries can surface prior analysis records associated with the local identity. <br>
Mitigation: Use separate workspaces or identities when report history should remain isolated. <br>
Risk: Visual aquarium plant symptoms can be ambiguous and may not fully determine water quality or nutrient causes. <br>
Mitigation: Treat the output as care guidance and combine it with water testing or expert review before making significant aquarium changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-plant-health-monitor-analysis) <br>
- [Aquarium Plant Health Monitor API documentation](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON report text with optional report export links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save report output to a local file when an output path is supplied.] <br>

## Skill Version(s): <br>
1.0.4 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
