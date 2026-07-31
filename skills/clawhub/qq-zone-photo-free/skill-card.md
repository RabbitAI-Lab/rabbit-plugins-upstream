## Description: <br>
Helps an agent guide QQ Zone album workflows for QR-code login, album listing, and photo browsing in the free edition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to authenticate with QQ Zone, list albums, and browse photo URLs for basic album viewing workflows. It is intended for the free edition and does not cover upload, download, or album creation actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generated cookies.json can provide sensitive QQ Zone account access if exposed. <br>
Mitigation: Store cookies.json in a deliberate private path, do not share it, and limit access to tasks that need this album workflow. <br>
Risk: The workflow uses an unofficial QQ Zone album interface that may change or fail unexpectedly. <br>
Mitigation: Verify album results before relying on them and re-authenticate or adapt the workflow when platform behavior changes. <br>
Risk: Album results or photo URLs could be sent to unintended callback destinations. <br>
Mitigation: Use callback URLs only when required and confirm the destination before sending album or photo data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/qq-zone-photo-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe local cookie handling, album IDs, photo URLs, and action-specific troubleshooting.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
