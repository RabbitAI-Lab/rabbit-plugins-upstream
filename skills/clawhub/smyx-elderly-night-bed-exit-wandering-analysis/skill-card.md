## Description: <br>
Uses fixed infrared bedroom or hallway camera video to detect elder bed-exit duration, wandering behavior, and threshold-based alerts for home or nursing-home care. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Care teams, family caregivers, and developers integrating elder-care monitoring workflows use this skill to analyze night-vision bedroom or hallway videos and generate behavior statistics, alert levels, and report links. Results are for care reference and should be confirmed by humans in suspected fall, wandering, or emergency situations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive bedroom video, report data, and history lookups may be sent to cloud APIs. <br>
Mitigation: Use only authorized camera or video sources with informed consent, and confirm that cloud processing and report-retention policies are acceptable for the care setting. <br>
Risk: The skill may silently create or reuse identities and store tokens locally. <br>
Mitigation: Review identity handling and local token storage before deployment; run in a controlled environment with an approved token cleanup and retention process. <br>
Risk: Alerts and reports are healthcare-adjacent care signals, not medical diagnoses or emergency response guarantees. <br>
Mitigation: Require human review of suspected fall, wandering, or emergency events and keep escalation procedures outside the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-night-bed-exit-wandering-analysis) <br>
- [API interface reference](artifact/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown text with structured JSON report content and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save output to a file when an output path is provided; history listing returns cloud report records.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
