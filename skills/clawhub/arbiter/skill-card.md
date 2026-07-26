## Description: <br>
Push decisions to Arbiter Zebu for async human review when an agent needs human input on plans, architectural choices, or approval before proceeding. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[5hanth](https://clawhub.ai/user/5hanth) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use Arbiter to hand off non-urgent planning, architecture, and approval decisions to a human reviewer through a local Arbiter Zebu review queue. It is most useful when an agent should pause for human judgment before continuing work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local review queue may contain decision context from agent sessions. <br>
Mitigation: Keep ~/.arbiter/queue/ private and review queued decision content before sharing or syncing it. <br>
Risk: Queue IDs should not be treated as security-sensitive credentials. <br>
Mitigation: Use an updated release before relying on generated queue IDs for security-sensitive workflows. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/5hanth/skills/arbiter) <br>
- [Arbiter Zebu Bot](https://github.com/5hanth/arbiter-zebu) <br>
- [Arbiter Zebu Architecture](https://github.com/5hanth/arbiter-zebu/blob/main/ARCHITECTURE.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown decision files in the local Arbiter queue with JSON CLI responses for push, status, and answer retrieval.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the arbiter-push CLI and writes decision context under ~/.arbiter/queue/.] <br>

## Skill Version(s): <br>
0.1.0 (source: release evidence and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
