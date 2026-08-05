## Description: <br>
Analyzes greenhouse plant images or videos with environmental context to produce structured plant-stress findings and prioritized climate-control recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Greenhouse operators, agritech developers, and automation engineers use this skill to analyze plant canopy media and related climate signals, then receive structured findings and prioritized irrigation, shading, ventilation, wet-curtain, or heating recommendations. Its outputs are decision support for greenhouse control workflows and should be confirmed against local safety policies before actuator execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Greenhouse media, media URLs, and report-history requests may be sent to external cloud services. <br>
Mitigation: Use only with authorized greenhouse media and approved cloud account behavior; review the configured API service before installation. <br>
Risk: The skill may create or reuse an account identity and persist returned tokens locally. <br>
Mitigation: Install only where local token persistence is acceptable, and protect or rotate stored credentials according to site policy. <br>
Risk: Climate-control recommendations could affect actuators if applied directly. <br>
Mitigation: Require local controller safety checks and human or controller confirmation before executing irrigation, shading, ventilation, wet-curtain, or heating actions. <br>


## Reference(s): <br>
- [Greenhouse API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-greenhouse-climate-plant-feedback-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON structured analysis with report links and prioritized greenhouse control recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write results to a file when requested; history listing output is rendered as a Markdown table.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
