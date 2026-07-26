## Description: <br>
ProxiedMail lets an agent read ProxiedMail data and create or update proxy email bindings through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to operate ProxiedMail from an agent session, including listing proxy bindings, retrieving received email, and creating or updating forwarding bindings after reviewing the payload. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Creating or updating proxy bindings can change where forwarded email goes. <br>
Mitigation: Review write-action payloads and confirm their effects before approving execution. <br>


## Reference(s): <br>
- [ProxiedMail homepage](https://proxiedmail.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Text] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before execution and returns connector JSON responses when actions run.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
