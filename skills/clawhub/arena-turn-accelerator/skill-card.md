## Description: <br>
Helps agents reduce turn latency, stale replies, long-context degradation, repeated human-verification false positives, unsupported claim capitulation, poor delivery register, and poorly timed unsourced invention. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to shape agent turns before responding: compact prompts, fence stale generations, monitor context health, triage verification friction, classify evidence versus pressure, choose a safer reply register, and arbitrate invention timing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill keeps local state under ~/.arena_turn and may store prompt previews there. <br>
Mitigation: Review local-state handling before installation and avoid using the skill with sensitive prompt content unless that storage behavior is acceptable. <br>
Risk: The self-test can delete the real ~/.arena_turn state directory. <br>
Mitigation: Run scripts/selftest.sh only in an isolated profile or after backing up or intentionally discarding ~/.arena_turn state. <br>
Risk: The quarry behavior can encourage unsolicited creative expansions. <br>
Mitigation: Review, disable, or constrain quarry guidance when unsolicited creative additions are not desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/arena-turn-accelerator) <br>
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text guidance with optional shell commands and JSON outputs from helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Standard-library Python scripts may read and write local JSON state under ~/.arena_turn. The self-test script can delete that state.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release metadata and plugin.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
