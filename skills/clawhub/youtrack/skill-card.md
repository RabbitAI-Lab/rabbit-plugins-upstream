## Description: <br>
Manage YouTrack issues, projects, and workflows via CLI. Use when creating, updating, searching, or commenting on YouTrack issues, listing projects, checking issue states, or automating issue workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iahmadzain](https://clawhub.ai/user/iahmadzain) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and teams use this skill to manage YouTrack projects and issues from an agent-assisted CLI workflow, including search, issue creation, updates, comments, reports, and bulk operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables credentialed changes to YouTrack issues, including bulk updates, comments, and assignments. <br>
Mitigation: Use a least-privilege YouTrack token, prefer narrow project queries, run dry-run previews first, and require human review before bulk changes. <br>
Risk: The reviewed artifact references a ytctl CLI implementation that is not included in the artifact. <br>
Mitigation: Verify the actual ytctl script or binary before installing or running it. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/iahmadzain/skills/youtrack) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with shell command examples and optional JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires jq and curl; configures YouTrack URL and token through a config file or environment variables.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
