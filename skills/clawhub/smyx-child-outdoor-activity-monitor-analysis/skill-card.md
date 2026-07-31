## Description: <br>
Monitors fixed-camera footage at a home entrance or balcony door to count a child's exits and returns, estimate daily outdoor duration, and produce insufficient-activity reminders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Families, schools, kindergartens, and developers building child health monitoring workflows use this skill to analyze entrance or balcony camera video and generate daily outdoor-duration reports and reminders. The output is based on visual door-transition events and should not be treated as medical advice or diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles child and home entrance or balcony video and may send it to the configured cloud service. <br>
Mitigation: Use only with explicit guardian consent, a clear retention and deletion plan, and privacy-preserving camera views where practical. <br>
Risk: The skill can create or reuse persistent local identity state and stores authentication-related data locally. <br>
Mitigation: Review the local workspace data directory before deployment and treat the SQLite database and related local state as credentials. <br>
Risk: Outdoor duration is estimated from door-transition events and does not prove actual exercise or health status. <br>
Mitigation: Review results as activity estimates only and avoid using the output for medical decisions or diagnosis. <br>


## Reference(s): <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-outdoor-activity-monitor-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON-like structured text with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include daily duration metrics, event counts, alert type, recommended action, historical report tables, and export links.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter and release changelog state 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
