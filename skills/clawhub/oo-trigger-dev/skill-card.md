## Description: <br>
Trigger.dev helps agents operate Trigger.dev through an OOMOL-connected account for reading run data and carrying out user-approved state-changing actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Trigger.dev action schemas, list and retrieve run data, fetch completed results, cancel or replay runs with confirmation, and trigger tasks through the oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Credentialed Trigger.dev actions can change run state or trigger tasks. <br>
Mitigation: Use scoped API tokens where possible and confirm exact payloads and expected effects before write or destructive actions. <br>
Risk: Commands can fail when authentication, Trigger.dev connection scope, or billing state is missing. <br>
Mitigation: Run setup steps only after the matching error and resolve authentication, app connection, or billing before retrying. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-trigger-dev) <br>
- [Trigger.dev homepage](https://trigger.dev) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Fetches live action schemas before constructing JSON payloads; write actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: artifact frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
