## Description: <br>
httpSMS (httpsms.com). Use this skill for ANY httpSMS request - reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to let an agent operate an OOMOL-connected httpSMS account through the oo CLI. It supports reading account, phone, message, thread, and billing usage data, plus sending SMS or MMS messages and deleting individual messages with explicit confirmation requirements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send real SMS or MMS messages through a registered httpSMS Android phone. <br>
Mitigation: Confirm the exact recipient, sender phone, message content, media payload, and expected effect with the user before running send_message. <br>
Risk: The skill can delete individual message records. <br>
Mitigation: Require explicit approval for the target message ID before running delete_message. <br>
Risk: Setup and connection commands may start authentication, connection, or billing recovery flows. <br>
Mitigation: Run oo CLI installation, login, app connection, or billing recovery steps only after a command fails with the matching setup, auth, connection, or billing error. <br>


## Reference(s): <br>
- [httpSMS homepage](https://httpsms.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Skill page](https://clawhub.ai/oomol/skills/oo-httpsms) <br>
- [Publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
