## Description: <br>
Analyzes 30-60 seconds of adult facial video with remote photoplethysmography (rPPG) to produce HRV metrics, trend signals, and health-adjacent monitoring reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and health-management teams use this skill to analyze adult still-face video or video URLs for HRV indicators such as SDNN, RMSSD, pNN50, LF/HF ratio, signal quality, and recent trend direction. It supports personal wellness trend monitoring, fatigue or stress prompts, and historical report lookup, but the artifact states that results are not medical diagnoses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes sensitive facial video and health-adjacent HRV data through a publisher cloud service. <br>
Mitigation: Use it only with informed consent, avoid third-party faces without permission, and review the publisher's data handling before using it for sensitive wellness monitoring. <br>
Risk: The security evidence notes automatic identity creation, report history access, and local token persistence. <br>
Mitigation: Confirm how reports, tokens, local workspace data, and account-linked history can be reviewed and deleted before deployment. <br>
Risk: The artifact frames HRV output as trend guidance rather than clinical assessment. <br>
Mitigation: Present outputs as wellness or signal-processing trends and do not use them as a substitute for ECG-based assessment or clinician diagnosis. <br>


## Reference(s): <br>
- [HRV API interface documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Text, Markdown, JSON, Files] <br>
**Output Format:** [Markdown report or JSON, with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes HRV metrics, trend indicators, signal quality, stress or fatigue prompts, report export links, and historical report listings when requested.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
