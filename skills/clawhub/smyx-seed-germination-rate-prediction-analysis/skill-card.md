## Description: <br>
Analyzes seedling tray images or videos to identify emerged seedlings, count germinated seeds, and estimate germination rate for incubators, greenhouse trays, home planting pots, and seed company tests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit seedling tray images, videos, or URLs for cloud-based germination counting, germination-rate estimation, structured report output, and report history lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Seed images, videos, URLs, and analysis results are processed through the LifeEmergence cloud service. <br>
Mitigation: Avoid sensitive media until the publisher clarifies consent, retention, deletion, and downstream processing controls for submitted content and reports. <br>
Risk: The skill may silently create or reuse a local identity and store authentication tokens in the workspace SQLite database. <br>
Mitigation: Run the skill in an isolated workspace, restrict access to workspace data files, and review or clear local identity and token storage before sharing the workspace. <br>
Risk: History lookup retrieves cloud report records associated with the resolved local identity. <br>
Mitigation: Avoid shared identities or shared workspaces for sensitive tests, and confirm the account scope before using history-list commands. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-seed-germination-rate-prediction-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [Seed Germination API Documentation](references/api_doc.md) <br>
- [Common Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON text with structured analysis results, history lists, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save output to a user-provided file path; requires a local media file, media URL, or history-list request.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
