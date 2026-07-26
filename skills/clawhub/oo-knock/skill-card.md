## Description: <br>
Operate Knock through an OOMOL-connected account for user lookup, user identification, permanent user deletion, and workflow triggering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect Knock action schemas, manage Knock users, and trigger Knock workflows through the OOMOL oo CLI connector. It is intended for Knock-connected accounts where read actions can run directly and state-changing actions are reviewed before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can change Knock user records or trigger workflows for one or more recipients. <br>
Mitigation: Confirm the exact action, recipients, and payload with the user before running write operations. <br>
Risk: The delete_user action permanently deletes a Knock user and associated data. <br>
Mitigation: Require explicit approval for the target user before running destructive deletion. <br>
Risk: Authentication, connector, or billing failures may require setup steps before actions can run. <br>
Mitigation: Use setup or connection steps only after the corresponding command failure occurs. <br>


## Reference(s): <br>
- [ClawHub Knock skill page](https://clawhub.ai/oomol/skills/oo-knock) <br>
- [Knock homepage](https://knock.app/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Schema-first action execution through oo connector commands; write and destructive actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence metadata and release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
