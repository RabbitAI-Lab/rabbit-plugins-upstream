## Description: <br>
Generate copy-paste bash scripts for Ralph Wiggum/AI agent loops (Codex, Claude Code, OpenCode, Goose). Use when asked for a "Ralph loop", "Ralph Wiggum loop", or an AI loop to plan/build code via PROMPT.md + AGENTS.md, SPECS, and IMPLEMENTATION_PLAN.md, including PLANNING vs BUILDING modes, backpressure, sandboxing, and completion conditions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[endogen](https://clawhub.ai/user/endogen) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to create and run monitored AI coding loops that plan work, implement tasks, run backpressure checks, and surface decisions, errors, or completion through OpenClaw notifications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is a disclosed autonomous coding loop with powerful defaults and notification behavior that require review before use. <br>
Mitigation: Install only for a dedicated repository or sandbox, review generated loop files and notification contents, and confirm that the automation is appropriate for the target project. <br>
Risk: Some documented agent flags can bypass or reduce normal approval boundaries. <br>
Mitigation: Override unsafe defaults before running the loop and prefer sandboxed execution with scoped workspace permissions. <br>
Risk: The RALPH_TEST environment variable is executed as shell code during loop iterations. <br>
Mitigation: Treat RALPH_TEST as arbitrary shell input and set it only to reviewed commands that are safe for the project environment. <br>
Risk: Systemd and sudo setup snippets can create host-level persistence. <br>
Mitigation: Use the persistence examples only when long-running host services are explicitly intended and have been reviewed. <br>


## Reference(s): <br>
- [Ralph pattern](https://ghuntley.com/ralph/) <br>
- [Monitored Ralph Loop on ClawHub](https://clawhub.ai/endogen/skills/monitored-ralph-loop) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with bash snippets, template files, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces loop setup instructions, prompt templates, agent context templates, and shell commands for Codex, Claude Code, OpenCode, or Goose.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
