## Description: <br>
cx-cli guides agents to use the cx CLI for semantic code navigation, including code structure overviews, symbol definitions, and reference tracing before reading or refactoring files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wei840222](https://clawhub.ai/user/wei840222) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to navigate large codebases with cx before reading full files, find definitions and references, and plan refactors with less context overhead. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate for broad code-navigation phrasing. <br>
Mitigation: Use it when semantic code navigation is intended, and fall back to direct file reading for unsupported files or full-context needs. <br>
Risk: Optional cargo or grammar installation commands can modify the local tool environment. <br>
Mitigation: Run installation commands only after confirming the cx package and requested grammars are trusted and needed. <br>
Risk: cx supports only installed grammars and does not parse Markdown, YAML, JSON, TOML, or unsupported source languages. <br>
Mitigation: Check file type, git root, and installed grammars before using cx; use read or text search when cx is not appropriate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wei840222/skills/cx-cli) <br>
- [cx Decision Tree](references/decision-tree.md) <br>
- [cx Output Examples](references/output-examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands; cx command output may be TOON or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the cx binary; optional cargo and language grammar installation commands may be suggested when needed.] <br>

## Skill Version(s): <br>
1.1.2 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
