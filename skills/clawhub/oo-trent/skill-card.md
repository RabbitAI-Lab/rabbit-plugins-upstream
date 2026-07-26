## Description: <br>
Trent (trent.ai). Use this skill for any Trent request involving reading, creating, or updating data through the OOMOL `oo` CLI connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to operate Trent through an OOMOL-connected account, especially to send chat messages and return assembled response content with thread metadata. The skill guides schema-first connector execution and setup recovery when authentication, connection, or billing errors occur. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sending a Trent chat message changes external account state. <br>
Mitigation: Confirm the exact message payload and intended effect with the user before running `send_chat`. <br>
Risk: Connector execution depends on the user's OOMOL authentication, Trent connection, and billing status. <br>
Mitigation: Run setup or billing recovery steps only after command errors indicate the matching auth, connection, or credit issue. <br>
Risk: Raw Trent credentials could be mishandled if the connector flow is bypassed. <br>
Mitigation: Use the OOMOL `oo` connector flow and do not request, expose, or directly handle raw Trent API tokens. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-trent) <br>
- [Trent homepage](https://trent.ai/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash, PowerShell, and JSON command examples; connector action responses are JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The `send_chat` action returns assembled response content plus thread metadata, with execution metadata under `meta.executionId`.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
