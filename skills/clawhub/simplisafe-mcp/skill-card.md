## Description: <br>
Query and control a SimpliSafe alarm system from the shell with curl, including system state, sensors, locks, events, settings, arming, disarming, locking, and unlocking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent inspect and operate a SimpliSafe home security system from shell commands. It is intended for account-specific alarm, sensor, lock, event, and settings workflows after the user provides SimpliSafe authentication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can arm, disarm, lock, and unlock a real home security system. <br>
Mitigation: Require explicit user confirmation before any command that changes alarm or lock state, and re-read the relevant state after the action. <br>
Risk: The SimpliSafe refresh token grants account access and should be treated like a password. <br>
Mitigation: Keep the token in a private environment variable or private .env file and avoid exposing it in logs, prompts, or shared output. <br>
Risk: Some settings endpoints can return alarm PINs in cleartext. <br>
Mitigation: Query PIN-bearing payloads only when the user explicitly asks for codes; otherwise project safer settings fields. <br>


## Reference(s): <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [SimpliSafe curl and jq recipes](artifact/references/recipes.md) <br>
- [SimpliSafe shell helpers](artifact/references/ss-helpers.sh) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplisafe-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON-processing examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce SimpliSafe API calls and jq filters that read account state or request physical alarm and lock actions.] <br>

## Skill Version(s): <br>
0.1.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
