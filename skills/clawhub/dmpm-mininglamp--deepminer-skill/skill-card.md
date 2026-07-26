## Description: <br>
Provides agent guidance and shell-command workflows for using dm-cli to interact with DeepMiner, submit user prompts, manage threads and asynchronous tasks, and retrieve task results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dmpm-mininglamp](https://clawhub.ai/user/dmpm-mininglamp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to route DeepMiner-related requests through dm-cli, preserve prompts and returned messages accurately, manage long-running DeepMiner threads, and handle asynchronous task lifecycle states. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends selected prompts, uploaded files, and task results to DeepMiner through dm-cli. <br>
Mitigation: Install and use it only when DeepMiner processing is intended, and avoid sending secrets, credentials, regulated data, or private file links unless that use is approved. <br>
Risk: DeepMiner asynchronous tasks and forced follow-up messages can consume account resources or interrupt in-progress work. <br>
Mitigation: Review task state before starting, stopping, or forcing task lifecycle actions, and confirm resource-sensitive async task starts with the user. <br>
Risk: A documented dm-cli parsing issue can affect task info responses when estimate_time is returned as a number. <br>
Mitigation: Use thread result or task lifecycle status checks as the documented fallback when task info parsing fails. <br>


## Reference(s): <br>
- [DeepMiner skill release page](https://clawhub.ai/dmpm-mininglamp/skills/deepminer-skill) <br>
- [thread.result response structure](references/response-structure.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include DeepMiner thread IDs, task IDs, status summaries, and links to generated task files.] <br>

## Skill Version(s): <br>
1.7.2 (source: server release evidence and changelog, released 2026-06-26) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
