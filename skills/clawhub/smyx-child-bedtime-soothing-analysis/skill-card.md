## Description: <br>
Through a fixed camera with infrared night vision and microphone in a child's bedroom, this skill analyzes night-time audio/video to detect pre-sleep crying, fear-of-dark behaviors, and post-nightmare awakenings, then returns structured soothing actions such as soft night-light settings, recorded parent audio, lullabies, parent alerts, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze authorized child bedroom or nursery audio/video during sleep windows, detect bedtime distress patterns, and produce structured reports and escalation guidance for soothing workflows. It is intended for behavioral detection and caregiver notification, not medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Children's bedroom audio/video or media URLs may be sent to a configured cloud service for analysis. <br>
Mitigation: Use only with explicit parental authorization, confirm who operates the backend, and verify retention, access control, and report-link sharing before deployment. <br>
Risk: The skill may create or reuse a persistent local identity and store account tokens locally. <br>
Mitigation: Run it in a controlled environment, limit local file access, rotate or revoke tokens as needed, and document how identity state can be cleared. <br>
Risk: Historical cloud reports may expose sensitive child sleep and bedroom activity data. <br>
Mitigation: Restrict report access to authorized caregivers, review cloud report history permissions, and avoid sharing exported links beyond approved recipients. <br>
Risk: The skill is positioned around child sleep behavior and could be mistaken for medical assessment. <br>
Mitigation: Present outputs as behavioral observations and caregiver guidance only, and direct repeated or severe sleep issues to qualified pediatric or child psychology professionals. <br>


## Reference(s): <br>
- [Child bedtime soothing API documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-bedtime-soothing-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON analysis report with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured distress classifications, soothing action recommendations, historical report tables, and report links.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter says 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
