## Description: <br>
Analyzes smart greenhouse plant imagery with optional environmental sensor context to produce plant stress findings and prioritized climate-control actions such as irrigation, shading, fan, wet-curtain, and heating commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Greenhouse operators and agricultural engineers use this skill to submit plant images, videos, or URLs and receive structured plant-state analysis, prioritized climate-control actions, resource-use suggestions, and cloud history report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Greenhouse images, videos, URLs, and analysis requests may be sent to an external lifeemergence cloud service. <br>
Mitigation: Use only media and URLs approved for external processing, and avoid private camera footage or sensitive operational data unless the publisher documents retention and handling practices. <br>
Risk: Reports are tied to an automatically managed identity and can be queried from cloud history. <br>
Mitigation: Confirm how identity creation, token storage, and report history are managed before installation, and restrict use to environments where this linkage is acceptable. <br>
Risk: The output proposes greenhouse control actions that may be unsuitable for local equipment or crop conditions. <br>
Mitigation: Treat recommendations as decision support and require local controller safeguards or human review before executing irrigation, shading, ventilation, wet-curtain, or heating actions. <br>


## Reference(s): <br>
- [Greenhouse API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-greenhouse-climate-plant-feedback-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON analysis report with command examples and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report links and prioritized greenhouse control actions; does not provide PID values or valve-opening percentages.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence; artifact frontmatter says 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
