## Description: <br>
Analyzes a local project directory to report programming language distribution, file counts, total lines, effective code lines, and optional JSON output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zmgood](https://clawhub.ai/user/zmgood) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect a codebase's language mix, line counts, and technology-stack composition. It can present a readable report with an ASCII distribution chart or JSON suitable for follow-on processing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Per-file detail or JSON output can reveal file paths and line-count metadata from the analyzed project. <br>
Mitigation: Run the analyzer only on folders the user intends to inspect, and review detailed or JSON output before sharing it outside the project context. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zmgood/skills/code-language-analyzer-claw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, guidance] <br>
**Output Format:** [Plain text report or JSON, with Markdown guidance from the agent] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Optional per-file detail and JSON export may include relative file paths and line-count metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
