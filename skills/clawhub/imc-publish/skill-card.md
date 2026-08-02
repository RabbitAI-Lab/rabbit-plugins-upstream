## Description: <br>
IMC Publish helps agents publish, schedule, and check social media posts through a user's InstallMyClaw workspace. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[junwei1213](https://clawhub.ai/user/junwei1213) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and operator agents use this skill to prepare, schedule, confirm, and monitor posts to social channels connected to the user's InstallMyClaw workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The built-in updater can replace installed skill files from an unsigned moving branch. <br>
Mitigation: Use the platform-managed updater when installed from ClawHub, or review the source before running the helper script's update command. <br>
Risk: A social post could be sent to the wrong platform, account, caption, media set, or schedule if the preview is not checked. <br>
Mitigation: Review the draft preview and confirm only intentionally requested posts with the expected targets, caption, media count, and timing. <br>
Risk: Publishing requires a workspace API key with access to connected social accounts. <br>
Mitigation: Store the key in an environment variable or secrets manager and never paste it into chat or write it into repository files. <br>


## Reference(s): <br>
- [Platform notes](references/platforms.md) <br>
- [IMC Publish ClawHub listing](https://clawhub.ai/junwei1213/skills/imc-publish) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON responses from the helper script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3 and an InstallMyClaw publishing key; publishing is confirmation-gated.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
