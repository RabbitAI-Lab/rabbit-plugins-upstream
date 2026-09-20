## Description:

This skill generates multiple AI agent role definitions from a natural-language prompt and produces organizational and collaboration diagrams for prototyping multi-agent systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[brandon-zhanghaodong](https://clawhub.ai/user/brandon-zhanghaodong)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to prototype multi-agent team structures from task descriptions and generate Mermaid and PNG org chart or swimlane artifacts for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says the skill overstates its behavior and should be reviewed before installation.

Mitigation: Review the packaged skill files and expected outputs before use, and install only in a disposable or tightly scoped workspace.

Risk: The security guidance warns that documented CLI behavior is unreliable unless argument parsing and output path scoping are fixed.

Mitigation: Use a trusted output directory, verify command-line arguments before execution, and constrain writable paths when running the scripts.

Risk: The scripts write predictable Mermaid and PNG filenames and rely on an external diagram renderer.

Mitigation: Run the workflow in an isolated directory and confirm the diagram renderer is trusted and available before processing outputs.

## Reference(s):

- [Reference Documentation for Multi Agent Orchestrator](references/api_reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with Python scripts that produce Mermaid code and PNG diagram files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes org_chart and swimlane outputs to a caller-specified output directory; PNG rendering depends on an external diagram renderer.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
