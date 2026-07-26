## Description: <br>
Instagram CLI for viewing feeds, posts, profiles, and engagement via cookies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arein](https://clawhub.ai/user/arein) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to operate the gram Instagram CLI for reading feeds, profiles, search results, and post details, and for intentional engagement actions with their own authenticated Instagram session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles live Instagram session cookies, which can grant access to an Instagram account. <br>
Mitigation: Treat Instagram cookies and browser profiles like passwords, and avoid putting tokens in shared configs, logs, screenshots, or shell history. <br>
Risk: Some gram commands can change account state by liking, saving, commenting, following, or unfollowing. <br>
Mitigation: Run engagement commands only when you intend to modify the account, and review commands before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/arein/skills/gram) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and optional plain text or JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the gram CLI and Instagram session cookies; engagement commands can change account state.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
