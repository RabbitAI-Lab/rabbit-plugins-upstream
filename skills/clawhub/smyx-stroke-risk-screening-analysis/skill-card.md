## Description: <br>
Analyzes face images or videos with optional physiological indicators to produce stroke-risk screening reports, warnings, lifestyle suggestions, and medical guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and health-support agents use this skill to screen stroke risk from face media plus optional blood pressure, blood sugar, and lipid values, returning a structured report and report-history links. Outputs are screening guidance only and are not a medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles facial media or URLs, health measurements, report-history requests, and identity tokens through the Life Emergence cloud service. <br>
Mitigation: Use only where the service privacy, retention, and medical-use terms are acceptable; avoid sensitive media unless authorized and clear local workspace data or tokens when identity reuse is not desired. <br>
Risk: Stroke-risk screening output may be mistaken for a clinical diagnosis. <br>
Mitigation: Treat outputs as screening information only and seek professional medical evaluation for high-risk or concerning results. <br>
Risk: ClawHub security evidence flags the release as suspicious because health data and identity handling are automatic and under-disclosed. <br>
Mitigation: Review before installing, confirm cloud endpoint configuration and data handling, and restrict use to approved environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-stroke-risk-screening-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface reference](artifact/references/api_doc.md) <br>
- [Shared API interface reference](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON structured screening report with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report-history listings and report export links when available.] <br>

## Skill Version(s): <br>
1.0.8 (source: ClawHub release metadata; artifact frontmatter reports 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
