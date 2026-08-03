## Description: <br>
Designs, debugs, evaluates, and hardens framework-agnostic AI agents across loop structure, tools, memory, context budget, cost, security, escalation, and production rollout. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to design, debug, evaluate, harden, and operate AI agents. It helps with tool schemas, memory design, cost controls, human approvals, security boundaries, releases, and regression tests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill preserves operational memory in local Clawic notes, which can accumulate agent design, evaluation, cost, release, server, contact, and subscription details over time. <br>
Mitigation: Install only when this local continuity behavior is wanted, keep the configured note paths scoped, and review those files periodically. <br>
Risk: Agent design work may involve prompts, traces, tool configs, or environment examples that contain credential values. <br>
Mitigation: Store only credential pointers such as environment variable names or secret-manager locations, and strip pasted secret values before writing local notes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/agents) <br>
- [Clawic skill page](https://clawic.com/skills/agents) <br>
- [Clawic](https://clawic.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with examples, tables, and inline code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or update local Clawic notes under configured paths while avoiding credential values.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
