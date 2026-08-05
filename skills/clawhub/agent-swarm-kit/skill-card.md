## Description: <br>
Design and operate a bounded OpenClaw multi-agent team for isolated specialist agents, explicit routing, parallel tasks, review handoffs, and hard limits on cost, delegation, and completion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vswarm-ai](https://clawhub.ai/user/vswarm-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to design and run small, auditable OpenClaw agent teams with isolated workspaces, explicit work contracts, routing checks, review handoffs, and teardown steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Multiple agents and external message channels can broaden access to files, tools, or conversations beyond the intended task. <br>
Mitigation: Set explicit agent, delegation, time, token, spend, tool, directory, channel, and external-action limits before creating agents. <br>
Risk: Credentials or channel tokens could be exposed if copied into prompts, shared markdown, workspace files, logs, or source control. <br>
Mitigation: Keep credentials in approved interactive, environment-backed, or secret-file storage and verify that config output, logs, workspaces, and shell history do not contain secret values. <br>
Risk: Unbounded delegation, circular handoffs, conflicting file edits, or repeated retries can produce unreliable results or excess cost. <br>
Mitigation: Use one orchestrator, one owner per workstream, one writer per file, objective acceptance tests, clear stop conditions, and central conflict resolution. <br>
Risk: External posting, payment, publishing, or destructive actions could happen without the intended human approval. <br>
Mitigation: Require explicit authorization and review for external side effects, and run harmless routing and permission tests before relying on connected agents. <br>


## Reference(s): <br>
- [OpenClaw Agent CLI](https://docs.openclaw.ai/cli/agents) <br>
- [OpenClaw Channel CLI](https://docs.openclaw.ai/cli/channels) <br>
- [Channel and Routing Checklist](templates/CHANNEL_CONFIG.md) <br>
- [Multi-Agent Operating Rules](templates/SWARMING_RULES.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/vswarm-ai/skills/agent-swarm-kit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and checklist templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes bounded operating rules, least-privilege channel setup, verification, and teardown checklists.] <br>

## Skill Version(s): <br>
1.1.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
