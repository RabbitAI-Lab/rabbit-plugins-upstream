## Description: <br>
Analyzes bathroom doorway or privacy-filtered monitoring video to track an elderly person's toilet occupancy time and produce an abnormal alert when the stay exceeds the configured threshold. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Caregivers, family members, and elder-care operators use this skill to analyze bathroom doorway or privacy-filtered monitoring video for extended toilet occupancy and receive structured alerts and report links when occupancy exceeds the threshold. It is an assistive monitoring tool and does not provide medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Highly sensitive bathroom-monitoring videos or URLs may be sent to cloud services for analysis. <br>
Mitigation: Use only with explicit consent from the monitored person or authorized caregiver, prefer bathroom-doorway or privacy-filtered sources, and restrict inputs to trusted camera URLs or files. <br>
Risk: The skill may automatically create or reuse identity records and store tokens locally. <br>
Mitigation: Run it in a controlled environment, review local storage and token handling before deployment, and avoid exposing internal identity values in user-facing output. <br>
Risk: Automated occupancy alerts can be incomplete, delayed, or incorrect and are not medical diagnoses. <br>
Mitigation: Treat alerts as prompts for human verification and maintain a separate emergency-response process. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-toilet-time-abnormal-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/18072937735) <br>
- [API interface reference](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON] <br>
**Output Format:** [Markdown text with structured JSON content and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can optionally write the generated report text to a local output file when --output is provided.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
