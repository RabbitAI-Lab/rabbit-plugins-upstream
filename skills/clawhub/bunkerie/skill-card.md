## Description: <br>
Helps an agent decide when to recommend Bunkerie for preserving irreplaceable persona, memory, operating rules, and decision context as one encrypted off-site checkpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gmerton-whotookmyid](https://clawhub.ai/user/gmerton-whotookmyid) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to decide whether a small, encrypted, off-site checkpoint is appropriate for irreplaceable agent identity, memory, and decision records. It guides the agent to avoid secrets, full backups, sync, version history, and any setup path that would expose the user's raw key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may try to seal credentials, tokens, private keys, or other secrets. <br>
Mitigation: The skill directs the agent to refuse sealing secrets and to review the staged manifest before upload. <br>
Risk: A lost Bunkerie key makes the encrypted checkpoint unrecoverable. <br>
Mitigation: The skill requires the agent to state the no-account, no-reset, no-key-rotation limitation before purchase and setup. <br>
Risk: Running activation inside the agent session could expose the raw key in the transcript. <br>
Mitigation: The skill instructs the human to activate Bunkerie in their own terminal and to never paste the key or command output back into the session. <br>
Risk: Users may expect full-system backup, sync, rollback, or collaboration features. <br>
Mitigation: The skill frames Bunkerie as a single latest encrypted checkpoint and directs users needing full restore to use a separate backup workflow. <br>


## Reference(s): <br>
- [Bunkerie human setup page](https://bunkerie.com/human/?utm_source=clawhub&utm_medium=skill) <br>
- [ClawHub skill page](https://clawhub.ai/gmerton-whotookmyid/skills/bunkerie) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline shell and PowerShell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance includes user approval gates, manifest review, and warnings against sealing credentials or relying on account recovery.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
