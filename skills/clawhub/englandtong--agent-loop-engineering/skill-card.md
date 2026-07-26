## Description: <br>
Executes authorized software goals through bounded AI coding loops with persistent state, staged timeboxes, evidence requirements, failure budgets, context controls, stop gates, and resumable handoffs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[englandtong](https://clawhub.ai/user/englandtong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to run scoped coding work through bounded implementation, verification, state recording, and handoff loops when goals and acceptance criteria are clear. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may make scoped coding changes and update project-local execution state. <br>
Mitigation: Install only for repositories where this behavior is intended, and provide clear acceptance criteria and protected boundaries before use. <br>
Risk: Sensitive or high-impact work can involve secrets, production data, destructive actions, privileged changes, or unclear authority. <br>
Mitigation: Use the skill's stop gates: stop before those actions, require explicit authority, and record approvals without storing secret values. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/englandtong/skills/agent-loop-engineering) <br>
- [Execution Loop](artifact/references/en/execution-loop.md) <br>
- [Evidence And Completion](artifact/references/en/evidence-and-completion.md) <br>
- [Safety And Context](artifact/references/en/safety-and-context.md) <br>
- [Automation And Handoff](artifact/references/en/automation-and-handoff.md) <br>
- [Legacy State Migration](artifact/references/en/migration.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports, project-local state updates, JSONL loop records, code changes, and shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update authorized project files, Docs/ACTIVE_PACKET.md, and Docs/LOOP_RUNS.jsonl while recording concise evidence.] <br>

## Skill Version(s): <br>
2.0.0 (source: SKILL.md, artifact/_meta.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
