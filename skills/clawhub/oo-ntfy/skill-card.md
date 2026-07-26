## Description: <br>
ntfy lets agents inspect ntfy connector schemas, retrieve account profile and usage details, and publish notification messages through the OOMOL oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate ntfy through an OOMOL-connected account, including account checks and notification publishing. It is suited for workflows that need ntfy messages without directly handling raw API tokens. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A publish_message action can send a notification to the wrong topic or with the wrong payload. <br>
Mitigation: Confirm the exact topic, message, and payload with the user before running publish_message. <br>
Risk: The skill depends on OOMOL as the credential broker for ntfy access. <br>
Mitigation: Use the skill only when the user is comfortable with OOMOL-managed credentials and the required ntfy connection. <br>
Risk: First-time setup may require installing the oo CLI with a platform-specific install command. <br>
Mitigation: Review the oo CLI install command before running it, and perform setup only after an auth, connection, or missing-command failure. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ntfy) <br>
- [ntfy homepage](https://ntfy.sh) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include oo CLI commands, connector schema guidance, and confirmation prompts for write actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
