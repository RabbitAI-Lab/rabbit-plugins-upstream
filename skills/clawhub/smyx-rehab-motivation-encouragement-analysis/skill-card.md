## Description: <br>
Analyzes rehabilitation training photos or videos to identify patient frustration and giving-up tendency signals, produce a structured assessment, and suggest motivation or escalation actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, rehabilitation technology teams, and care teams use this skill to analyze authorized rehab training media for frustration or giving-up behaviors, generate structured monitoring results, and support timely encouragement or clinician/caregiver escalation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patient rehabilitation media and identity data may be sent to a configured cloud service. <br>
Mitigation: Use only with explicit patient or caregiver authorization, and review backend handling, retention, and access practices before installation. <br>
Risk: The skill can create local identity or token state in the workspace. <br>
Mitigation: Run it in a controlled workspace, restrict file access, and review or clear generated identity/token files according to local policy. <br>
Risk: Historical reports may be queried automatically from the cloud service. <br>
Mitigation: Limit use to authorized operators and confirm that historical-report access aligns with patient consent and organizational privacy requirements. <br>
Risk: Frustration and giving-up assessments can be mistaken or incomplete. <br>
Mitigation: Treat results as supportive behavioral signals, not medical diagnosis, and require qualified human review for clinical decisions or training-plan changes. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-rehab-motivation-encouragement-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown and JSON-style structured text with optional saved result file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call cloud APIs, query historical reports, and write an optional output file when requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
