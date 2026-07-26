## Description: <br>
Telnyx lets an agent inspect Telnyx connector schemas and run Telnyx messaging actions through the OOMOL oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to list and retrieve Telnyx messaging profiles and messages, and to send SMS or MMS messages from an OOMOL-connected Telnyx account after confirming write payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sending Telnyx messages can affect recipients or incur account costs. <br>
Mitigation: Confirm the exact recipient, message content, media URLs, and payload with the user before running send_message. <br>
Risk: Connector commands require an authenticated OOMOL account with an active Telnyx connection. <br>
Mitigation: Run setup or reconnection steps only after a command fails with an authentication, missing scope, expired credential, app readiness, or billing error. <br>


## Reference(s): <br>
- [ClawHub Telnyx Skill](https://clawhub.ai/oomol/skills/oo-telnyx) <br>
- [Telnyx Homepage](https://telnyx.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, text] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may return JSON from the oo CLI; write actions require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence.release.version and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
