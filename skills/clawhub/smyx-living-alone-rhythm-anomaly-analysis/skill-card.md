## Description: <br>
Analyzes fixed-camera night video for a person living alone to detect lights-off timing and early-morning movement against a 7-14 day baseline, then reports rhythm anomaly reminders without providing medical diagnoses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, family members, community workers, and developers use this skill to analyze consented night video from living-alone home-care settings, compare observed sleep-rhythm signals with a personal baseline, and produce reminders or historical report views for follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes highly sensitive home night video through cloud services and stores historical analysis reports. <br>
Mitigation: Use only with clear consent from the monitored person or legal guardian; confirm retention, access controls, export-link handling, and app-alert recipients before deployment. <br>
Risk: The skill silently creates or reuses an account identity and stores authentication tokens in the workspace data area. <br>
Mitigation: Review the account identity used for each deployment and decide whether local token storage in the workspace data directory is acceptable for the environment. <br>
Risk: Sleep-rhythm anomaly alerts can be caused by benign events and are not medical diagnoses. <br>
Mitigation: Treat results as visual rhythm parameters and deviation reminders; verify recurring anomalies with family, community staff, or qualified care providers. <br>


## Reference(s): <br>
- [API interface documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Structured text or JSON, with Markdown tables and report links for historical report lists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the returned analysis content to a user-selected output file.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence; artifact frontmatter: 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
