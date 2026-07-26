## Description: <br>
AI project management powered by CellCog with knowledge workspaces, document upload, AI-processed context trees, signed URL retrieval, and standalone or CellCog chat context workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nitishgargiitd](https://clawhub.ai/user/nitishgargiitd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create CellCog project workspaces, upload and process documents, inspect context tree markdown, and share temporary signed document URLs for project work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded local files are sent to CellCog for processing and may consume credits. <br>
Mitigation: Upload only intended project documents, confirm file scope before upload, and account for credit usage. <br>
Risk: Signed document URLs grant temporary unauthenticated access to project files. <br>
Mitigation: Use the shortest practical expiration, share URLs only with intended recipients, and avoid logging or broadly posting them. <br>
Risk: A signed URL remains valid until its expiration even if project access changes later. <br>
Mitigation: Choose short expirations for sensitive files and regenerate access only when current sharing is still intended. <br>


## Reference(s): <br>
- [CellCog](https://cellcog.ai) <br>
- [Project Management Cellcog on ClawHub](https://clawhub.ai/nitishgargiitd/skills/project-management-cellcog) <br>
- [Publisher profile: nitishgargiitd](https://clawhub.ai/user/nitishgargiitd) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown with Python and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, CELLCOG_API_KEY, and CellCog SDK access; generated signed URLs are time-limited.] <br>

## Skill Version(s): <br>
1.0.11 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
