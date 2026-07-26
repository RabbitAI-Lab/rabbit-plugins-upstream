## Description: <br>
Operate the Message-in-a-Bottle (MIAB) LIFO callback stack for asynchronous inter-agent delegation, return, resolution, cancellation, listing, and stale-callback reaping. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[albzhu](https://clawhub.ai/user/albzhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to manage file-based MIAB callback lifecycles so delegated agent work can be resumed without polling. It provides guidance and commands for registering wake targets, creating and forwarding callback stacks, returning results, resolving or cancelling callbacks, listing active work, and reaping stale bottles. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Callback state and wake routing are stored and mutated on disk without clear access-control or integrity safeguards. <br>
Mitigation: Use a private CLAW_HOME directory, restrict filesystem permissions, and run the broker only where agents with access to callback state are trusted. <br>
Risk: Callback summaries, results, and ledger entries may expose sensitive task context if agents include secrets or private data. <br>
Mitigation: Avoid placing secrets in callback summaries, resume contexts, results, artifacts, or ledger-retained final notes. <br>
Risk: The reaper, cancel, return, resolve, and wake flows can alter or route active agent work. <br>
Mitigation: Review callback state before running mutating commands and only enable reaper or wake automation for trusted agents and scheduler contexts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/albzhu/skills/miab-broker) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON, text] <br>
**Output Format:** [Markdown guidance with shell commands and JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands read and mutate callback state under CLAW_HOME/state/callbacks and may emit dispatch messages for agent wake routing.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
