## Description: <br>
Mixpost helps agents schedule and manage social media content across multiple platforms through a self-hosted Mixpost workspace. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lao9s](https://clawhub.ai/user/lao9s) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and content operations teams use this skill to configure Mixpost API access and have an agent retrieve accounts, manage media and tags, and create, schedule, approve, update, or delete posts. It is intended for workflows where an authenticated agent assists with social media content management in a Mixpost workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A powerful Mixpost token can allow an agent to create, publish, schedule, upload, update, or delete social media content. <br>
Mitigation: Use the least-privileged token available, confirm the workspace UUID, and require explicit confirmation before publishing, scheduling, approving, uploading, updating, or deleting posts or media. <br>
Risk: The Mixpost access token can expose workspace control if copied into logs, shared files, or chat transcripts. <br>
Mitigation: Keep the token in environment variables or a secret manager, avoid echoing it in command output, and rotate it if exposure is suspected. <br>


## Reference(s): <br>
- [Mixpost homepage](https://mixpost.app) <br>
- [ClawHub skill page](https://clawhub.ai/lao9s/skills/mixpost) <br>
- [Publisher profile](https://clawhub.ai/user/lao9s) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with curl examples and environment variable setup] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses MIXPOST_URL, MIXPOST_ACCESS_TOKEN, and MIXPOST_WORKSPACE_UUID to target a specific Mixpost instance and workspace.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
