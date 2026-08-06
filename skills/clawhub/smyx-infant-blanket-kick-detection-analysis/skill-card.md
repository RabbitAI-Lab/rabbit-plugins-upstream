## Description: <br>
Analyzes crib night-camera images or videos to estimate infant blanket coverage, detect kicking or blanket-slip events, and return alerts and structured reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Parents, caregivers, and developers of baby-monitoring workflows can use this skill to submit crib night-camera media or URLs for blanket-coverage analysis, kicking-event detection, alerting, and cloud report lookup. Results are auxiliary monitoring signals and do not replace adult supervision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Infant videos or supplied video URLs may be sent to lifeemergence.com cloud services. <br>
Mitigation: Use only with guardian consent, approved data-handling controls, and clear retention and deletion expectations. <br>
Risk: The skill may create or reuse an internal identity, retrieve cloud report history, and persist account tokens locally. <br>
Mitigation: Review token storage and account behavior before deployment, restrict runtime access, and clear local credentials when they are no longer needed. <br>
Risk: Visual coverage alerts can be incomplete, delayed, or incorrect and are not medical advice. <br>
Mitigation: Treat outputs as auxiliary monitoring signals, maintain adult supervision, and review alerts before acting on them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-blanket-kick-detection-analysis) <br>
- [Infant Blanket Kick Detection API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with optional JSON-detail output and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save output to a file when an output path is provided; report history is retrieved from cloud services.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
