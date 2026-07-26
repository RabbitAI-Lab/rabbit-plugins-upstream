## Description: <br>
Publishes, schedules, and checks social posts and small media through a user's InstallMyClaw workspace for connected Instagram, TikTok, Facebook, YouTube, LinkedIn, Threads, Google Business, and Telegram accounts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[junwei1213](https://clawhub.ai/user/junwei1213) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, operators, and agents use this skill to draft, preview, publish, schedule, and check status for social media content through connected accounts in an InstallMyClaw workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The built-in update command can replace installed skill files from a moving GitHub branch without signature verification. <br>
Mitigation: Prefer ClawHub/OpenClaw-managed updates, and do not run the update subcommand unless the source it will install has been reviewed. <br>
Risk: The skill can publish or schedule content to connected social accounts after confirmation. <br>
Mitigation: Create a draft, show the returned preview, wait for explicit confirmation for that draft, and report only API-confirmed post IDs and statuses. <br>
Risk: The publishing API key authorizes access to the user's workspace publishing service. <br>
Mitigation: Store the key in an environment variable or secrets manager, never paste it into chat, and never write it into repository files. <br>


## Reference(s): <br>
- [IMC Publish on ClawHub](https://clawhub.ai/junwei1213/skills/imc-publish) <br>
- [Platform Notes](references/platforms.md) <br>
- [InstallMyClaw Dashboard](https://dashboard.installmyclaw.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an IMC_PUBLISH_API_KEY and explicit human confirmation before publishing a draft.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
