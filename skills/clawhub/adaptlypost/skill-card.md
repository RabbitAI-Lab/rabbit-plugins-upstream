## Description: <br>
Schedule and manage social media posts across Instagram, X (Twitter), Bluesky, TikTok, Threads, LinkedIn, Facebook, Pinterest, and YouTube using the AdaptlyPost API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tarasshyn](https://clawhub.ai/user/tarasshyn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, marketers, creators, and developers use this skill to draft, schedule, publish, inspect, and manage social media posts across connected AdaptlyPost accounts. It is intended for agent-assisted social posting workflows that require explicit confirmation before public write actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Posts can become public, attributable, and difficult to fully retract. <br>
Mitigation: Require an explicit confirmation covering content, connected accounts, timing, and visibility before each post; prefer drafts when the user is uncertain or content is sensitive. <br>
Risk: The API token can act on every social account connected to the AdaptlyPost account group. <br>
Mitigation: Use a dedicated revocable token and connect only the accounts the agent needs for the workflow. <br>
Risk: Media uploaded through presigned URLs becomes publicly reachable once the upload completes, even if no post is created. <br>
Mitigation: Confirm exact file paths before upload, avoid broad directories without per-file approval, and upload only files the user named. <br>
Risk: Bulk or unattended scheduling can amplify mistakes across many accounts or posts. <br>
Mitigation: Confirm a small first batch for multi-post sessions and default unattended runs to drafts unless the exact recurring workflow was pre-authorized. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tarasshyn/skills/adaptlypost) <br>
- [AdaptlyPost homepage](https://adaptlypost.com) <br>
- [AdaptlyPost API reference](references/api-reference.md) <br>
- [AdaptlyPost platform configs](references/platform-configs.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown guidance with JSON and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ADAPTLYPOST_API_KEY; posting and media-upload workflows require explicit user confirmation before write actions.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata; artifact frontmatter reports 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
