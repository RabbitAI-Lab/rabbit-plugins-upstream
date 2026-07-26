## Description: <br>
Analyzes pet water-fountain videos or URLs through server-side APIs to estimate drinking frequency, session duration, daily intake, historical baseline changes, and abnormal intake alerts without providing diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, pet-care product teams, and developers use this skill to submit water-fountain video evidence and receive structured drinking-behavior metrics, historical report links, and abnormal intake alerts for pet health monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet videos or video URLs are sent to lifeemergence.com services for analysis and historical report retrieval. <br>
Mitigation: Submit only footage and URLs the user is permitted to share, and review privacy expectations before installation or use. <br>
Risk: The skill can silently create or reuse a local identity and store reusable account tokens in a workspace SQLite database. <br>
Mitigation: Run the skill in a controlled workspace, protect workspace data, and clear local data when the identity or tokens should not persist. <br>
Risk: Water-intake estimates and health-risk alerts can be mistaken for medical diagnosis. <br>
Mitigation: Treat results as informational monitoring signals and defer diagnosis or treatment decisions to a qualified veterinarian. <br>


## Reference(s): <br>
- [Pet Water Fountain Intake Analysis API Documentation](references/api_doc.md) <br>
- [Common Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-water-fountain-intake-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON structured analysis report with optional report export link] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save output to a requested local file; local video inputs must be mp4/avi/mov and 10 MB or smaller.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
