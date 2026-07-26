## Description: <br>
Agent Avengers is a multi-agent orchestration skill that decomposes complex tasks, assigns specialist agents, executes work in parallel or sequence, and consolidates the results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oozoofrog](https://clawhub.ai/user/oozoofrog) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to coordinate larger tasks across researcher, analyst, writer, coder, reviewer, and integrator agents. It is intended for workflows such as competitor analysis, app development, research synthesis, and multi-step content or code production. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can delegate broad tasks across multiple agents and profiles, which can amplify unclear instructions or unintended actions. <br>
Mitigation: Use explicit bounded prompts, set clear success criteria, and review the generated plan before dispatching work. <br>
Risk: Generated session commands may spawn or message agents with access to local files, tools, or long-running workflows. <br>
Mitigation: Review sessions_spawn and sessions_send commands before running them, avoid credentials or sensitive private data, and set appropriate timeouts. <br>
Risk: Mission outputs and cleanup behavior may leave temporary sessions or artifacts behind. <br>
Mitigation: Verify output paths before execution and manually confirm cleanup of spawned sessions and mission artifacts after completion. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oozoofrog/skills/agent-avengers) <br>
- [README](artifact/README.md) <br>
- [Korean README](artifact/README-kr.md) <br>
- [Announcement](artifact/ANNOUNCEMENT.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown, JSON plans, generated command snippets, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create mission plans, execution commands, progress summaries, and consolidated reports for multi-agent workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter, package.json, ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
