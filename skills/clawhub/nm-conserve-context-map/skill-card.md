## Description: <br>
Generates a compressed project context map to avoid expensive Read/Grep calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill at the start of a session or before implementation work to summarize project structure, dependencies, routes, entry points, environment variables, hot files, and other context for an unfamiliar codebase. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill scans the current repository and may expose project structure, dependencies, routes, environment variable names, and other local context in its output. <br>
Mitigation: Use it only in repositories where this inspection is acceptable, and review generated context before sharing it outside the working environment. <br>
Risk: The scanner may create .codesight/ context files during normal use. <br>
Mitigation: Use --no-wiki when a read-only scan is preferred, and review or ignore .codesight/ in version control if files are generated. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-context-map) <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown project overview with optional JSON output and optional .codesight/ files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports section-focused output, token limits, blast-radius checks, and an option to skip wiki file generation.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
