## Description: <br>
Save selected notes to Flomo through a user-configured Flomo inbox webhook. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiaoluoboding](https://clawhub.ai/user/xiaoluoboding) <br>

### License/Terms of Use: <br>


## Use Case: <br>
OpenClaw users and agents use this skill to save selected note text into a Flomo inbox for personal knowledge capture. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected note text is sent over the network to the configured Flomo webhook. <br>
Mitigation: Send only notes intended for Flomo and avoid secrets or highly sensitive content. <br>
Risk: Anyone with the Flomo webhook URL can post to the inbox. <br>
Mitigation: Store FLOMO_WEBHOOK_URL as a private environment variable and do not paste it into prompts, logs, or shared files. <br>
Risk: Passing note text as a command argument can expose content in shell history or process listings. <br>
Mitigation: Provide note text to the script on stdin, matching the script behavior. <br>


## Reference(s): <br>
- [Flomo](https://flomoapp.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Text] <br>
**Output Format:** [Shell command invocation with plain-text status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires FLOMO_WEBHOOK_URL; sends selected note text to Flomo and appends an OpenClaw tag.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
