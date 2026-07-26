## Description: <br>
Roam HQ lets agents read Roam HQ data and send reviewed bot messages through an OOMOL-connected account using the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect Roam HQ magicasts, public groups, and meeting recordings, and to send reviewed bot messages to a Roam HQ group through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A send_message payload could post unintended content to a Roam HQ group. <br>
Mitigation: Review the exact payload and expected effect with the user before approving the write action. <br>
Risk: The skill operates through the user's OOMOL-connected Roam HQ account. <br>
Mitigation: Install and use it only when the user intends Codex to access that connected account. <br>
Risk: First-time use may fail if the oo CLI is not installed or the OOMOL/Roam connection is not ready. <br>
Mitigation: Follow setup steps only after an auth, connection, or command-not-found failure. <br>


## Reference(s): <br>
- [ClawHub Roam HQ skill](https://clawhub.ai/oomol/skills/oo-roam) <br>
- [Roam HQ homepage](https://ro.am) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the oo CLI and an OOMOL-connected Roam HQ account; message-sending payloads require user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence release, skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
