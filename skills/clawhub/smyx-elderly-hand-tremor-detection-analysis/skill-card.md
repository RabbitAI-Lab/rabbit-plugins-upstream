## Description: <br>
Analyzes fixed-camera videos or video URLs of an elderly person's resting hand to detect periodic tremor motion, estimate frequency and amplitude, and produce a screening-oriented risk report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and care-workflow builders can use this skill to connect elderly hand-resting video inputs to a structured tremor screening report for home care, nursing home, or community health scenarios. It is intended to support early attention and follow-up, not to replace professional neurological diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive elderly health video data or video URLs are sent to external LifeEmergence services for analysis. <br>
Mitigation: Use only with informed consent from the monitored person or authorized caregiver, and avoid submitting videos unless that cloud processing is acceptable. <br>
Risk: The skill can silently create or reuse a persistent local or cloud user identity and link analysis history to it. <br>
Mitigation: Confirm that account linkage and report-history access match the user's privacy expectations before installation or use. <br>
Risk: The output is a screening-oriented risk report and may be misunderstood as a clinical diagnosis. <br>
Mitigation: Present results as objective video-motion indicators and encourage professional neurological evaluation for concerning findings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-hand-tremor-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](artifact/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON analysis report with tremor metrics, risk level, follow-up prompt, and report link when available] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the report to a user-specified output file and can return a Markdown table of cloud history reports.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
