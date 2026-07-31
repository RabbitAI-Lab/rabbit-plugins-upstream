## Description: <br>
This skill analyzes rehabilitation-session video, with optional audio and history signals, to identify patient frustration or giving-up behaviors and produce encouragement actions, progress comparisons, alerts, and reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External care teams and developers use this skill to analyze consented rehabilitation training media for behavioral frustration signals, generate structured reports, and suggest motivational escalation steps for human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive patient media while contacting cloud services and exporting reports. <br>
Mitigation: Use only with patient or guardian consent, organizational approval, reviewed endpoint and retention terms, and access controls appropriate for patient data. <br>
Risk: The security evidence says the skill silently creates or reuses identities and stores account tokens. <br>
Mitigation: Install in an isolated workspace, review local token storage before use, and avoid real patient video until disclosure and access-control requirements are approved. <br>
Risk: Automated encouragement or progress comparisons could mislead patients if outputs are treated as diagnosis or if progress data is overstated. <br>
Mitigation: Keep outputs as behavioral assessment and motivation guidance for human review, avoid medical diagnoses, and base progress comparisons only on verified historical records. <br>


## Reference(s): <br>
- [API interface documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-rehab-motivation-encouragement-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown and JSON analysis output with report links and optional saved result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local file or URL input, optional history listing, and basic, standard, or JSON detail levels.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
