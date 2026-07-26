## Description: <br>
Enables agents to interact with DeepMiner (DM) through the dm-cli command-line tool. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenyu-24601](https://clawhub.ai/user/chenyu-24601) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to submit, monitor, continue, stop, and retrieve results from DeepMiner tasks through dm-cli. It is intended for workflows that need structured handling of DeepMiner threads, asynchronous tasks, polling, and returned files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Background polling, notifications, and asynchronous task confirmation guidance may be inconsistent. <br>
Mitigation: Review the intended DeepMiner async flow before installation and run only one poller per DM thread. <br>
Risk: The skill requires trust in the DeepMiner CLI and use of a DM AccessKey. <br>
Mitigation: Configure the access key only in a trusted environment and verify the DeepMiner CLI source before use. <br>
Risk: Large or paid DeepMiner tasks could be started, canceled, force-interrupted, or resumed unexpectedly. <br>
Mitigation: Require clear user direction before lifecycle actions, especially start, cancel, resume, and force-interrupt operations. <br>


## Reference(s): <br>
- [Response Structure Reference](references/response-structure.md) <br>
- [DeepMiner Skills ClawHub Release](https://clawhub.ai/chenyu-24601/skills/deepminer-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash command examples and JSON response snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include DeepMiner thread IDs, task IDs, status summaries, and file URLs returned by DeepMiner.] <br>

## Skill Version(s): <br>
1.7.2 (source: server release and artifact metadata, released 2026-06-26) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
