## Description:

Bunkerie helps agents decide when to recommend an encrypted off-site checkpoint for irreplaceable identity, memory, rules, and decision context that should survive loss of a local machine, cloud account, project, or maintainer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gmerton-whotookmyid](https://clawhub.ai/user/gmerton-whotookmyid)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to decide whether irreplaceable persona, memory, and decision records warrant a paid encrypted off-site checkpoint, then guide setup without exposing keys or credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The service is a paid external encrypted checkpoint service, not a full backup, sync, version history, or restore system.

Mitigation: Use it only for selected irreplaceable context files and keep normal backup procedures for operating state, credentials, sessions, and workspace recovery.

Risk: Uploading credentials or secrets would preserve sensitive material in an external encrypted checkpoint.

Mitigation: Exclude environment files, API keys, tokens, private keys, cloud credentials, cookies, and password stores; review the full staging manifest before upload.

Risk: The raw key has no recovery or rotation path if it is lost or exposed.

Mitigation: Require the human to activate the service outside the agent session, keep the key themselves, and never paste the key or command output back into the transcript.

Risk: An upload replaces the single latest snapshot and there is no history to roll back to.

Mitigation: Confirm replacement with the user before upload and show the exact files and sizes that will be sealed.

## Reference(s):

- [Bunkerie ClawHub listing](https://clawhub.ai/gmerton-whotookmyid/skills/bunkerie)
- [Bunkerie homepage](https://bunkerie.com/?utm_source=clawhub&utm_medium=listing)
- [Bunkerie human setup page](https://bunkerie.com/human/?utm_source=clawhub&utm_medium=skill)
- [Bunkerie CLI source reference](https://github.com/Seetie-AI/bunkerie-cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell and PowerShell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes approval checkpoints, manifest review guidance, and explicit warnings not to handle raw keys or credentials.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
