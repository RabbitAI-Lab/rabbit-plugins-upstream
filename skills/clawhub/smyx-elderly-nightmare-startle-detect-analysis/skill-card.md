## Description: <br>
Analyzes fixed-camera infrared bedroom sleep audio/video to identify sudden sitting up, screams, arm thrashing, and related nighttime abnormal events, then reports event timing, frequency, duration, and caregiver-oriented recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, family members, and elder-care operators use this skill to review nighttime sleep audio/video for behavioral event summaries, trends, and non-diagnostic follow-up guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles highly sensitive bedroom sleep audio/video, identifiers, report links, and report history through cloud APIs. <br>
Mitigation: Use only with the elderly person's informed consent, review the configured cloud services before installation, and treat report links and history as sensitive records. <br>
Risk: Local token storage and cloud retention implications may be unclear to deployers. <br>
Mitigation: Review local token handling and cloud retention practices before using private footage. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/18072937735/skills/smyx-elderly-nightmare-startle-detect-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON analysis reports with event timelines, risk signals, recommendations, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report links and historical report tables; does not provide medical diagnosis.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter states 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
