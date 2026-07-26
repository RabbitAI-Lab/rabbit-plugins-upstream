## Description: <br>
Automatically detects electric motorcycles and e-bikes in restricted areas from video streams, images, local files, or media URLs, then reports counts, violation levels, alerts, and management suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Security operators, facilities teams, and their agents use this skill to analyze surveillance images, videos, or media URLs for electric motorcycle and e-bike activity in restricted areas, then review violation counts and handling suggestions. The skill can also retrieve identity-linked historical analysis reports from the configured cloud service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Surveillance images, videos, media URLs, and report queries are sent to the configured LifeEmergence cloud service. <br>
Mitigation: Use the skill only with media that is approved for external cloud processing, and confirm privacy, retention, and data-processing terms before deployment. <br>
Risk: The skill silently creates or reuses an account identity for analysis and historical report access. <br>
Mitigation: Review whether silent account creation and identity-linked report retrieval are acceptable for the target environment, and restrict execution to approved workspaces. <br>
Risk: Authentication tokens may be persisted locally in the workspace data database. <br>
Mitigation: Protect the workspace data directory, rotate tokens if access is suspected, and clear stored credentials before sharing or archiving the workspace. <br>
Risk: Detection results may be used to assess real-world violations from surveillance media. <br>
Mitigation: Treat outputs as operational decision support and require human review before enforcement or disciplinary action. <br>


## Reference(s): <br>
- [Electric Vehicle Detection API Documentation](references/api_doc.md) <br>
- [Generic Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-electric-vehicle-detection-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files] <br>
**Output Format:** [Markdown report text or structured JSON, with optional saved output files and cloud report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports basic, standard, and JSON detail levels; local media input is limited to configured supported formats and file size.] <br>

## Skill Version(s): <br>
9.9.10 (source: ClawHub release evidence; artifact frontmatter reports 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
