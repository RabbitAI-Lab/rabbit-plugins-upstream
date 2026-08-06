## Description: <br>
Recommends context compression strategies for bloated or quota-heavy sessions <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to analyze bloated or quota-heavy sessions, choose a context-reduction strategy, and estimate savings before task transitions or debugging work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Saved session notes or archived context could include secrets or private content if users preserve state without review. <br>
Mitigation: Review saved notes and archives before retaining or sharing them, and remove secrets or private content before using clear, archive, or catchup workflows. <br>
Risk: Delegating work or spawning continuation agents can expose task context beyond the current session boundary. <br>
Mitigation: Use continuation or delegation only when it fits the task and the shared context is appropriate for the receiving agent. <br>
Risk: Compression can remove or distort details needed for log debugging. <br>
Mitigation: Filter logs at the source and measure token savings before using compression; keep original logs available when full fidelity is required. <br>


## Reference(s): <br>
- [Log Debugging Hygiene](modules/log-debugging-hygiene.md) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-compression-strategy) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown guidance with command examples and recommended workflow steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces recommendations only; no bundled code executes automatically.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
