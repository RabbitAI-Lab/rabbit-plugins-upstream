## Description: <br>
Error Guard is an OpenClaw control-plane safety skill that helps agents inspect task state, stop active work, recover from unresponsive states, and isolate long-running worker activity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[amar1432](https://clawhub.ai/user/amar1432) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to manage long-running or high-risk OpenClaw tasks with status checks, emergency cancellation, recovery commands, watchdog evaluation, and event-driven worker isolation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can terminate active sessions broadly through emergency control commands. <br>
Mitigation: Restrict or review /flush and /recover before autonomous use, and install the skill only where callers are trusted to operate control-plane recovery tools. <br>
Risk: The skill includes an under-documented helper for spawning isolated sub-agents. <br>
Mitigation: Disable or scope the sub-agent spawning helper unless delegated long-running work is explicitly needed and monitored. <br>


## Reference(s): <br>
- [Error Guard ClawHub Skill Page](https://clawhub.ai/amar1432/skills/error-guard) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with TypeScript helper modules and JSON-like control responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes /status, /flush, and /recover control commands, task event helpers, watchdog actions, and worker-spawning guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
