## Description:

Generate, revise, validate, and render official WaveDrom diagrams from natural-language timing descriptions, protocol requirements, timing tables, or existing WaveJSON/JSON5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[siliconpeasant](https://clawhub.ai/user/siliconpeasant)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to turn timing descriptions, protocol requirements, timing tables, or existing WaveJSON/JSON5 into editable WaveJSON/JSON5 and rendered WaveDrom diagrams for digital timing, bus, protocol, register, and logic documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated timing diagrams can be syntactically renderable while still misrepresenting protocol timing or implementation semantics.

Mitigation: Build a timing contract, disclose assumptions, run validation, and reconcile the rendered diagram against the authoritative specification, RTL, trace, or timing table.

Risk: The render workflow writes local output files and may replace existing files when overwrite behavior is explicitly enabled.

Mitigation: Choose output directories intentionally, preserve editable JSON5 source, and enable overwrites only when replacement is intended.

Risk: Optional MCP registration changes the agent configuration for supported clients.

Mitigation: Review the registration step first, use dry-run output when appropriate, and force replacement only when an existing registration should be replaced.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/siliconpeasant/skills/wavedrom-gen)
- [Official WaveJSON reference](references/wavejson-official.md)
- [Protocol clarification and defaults](references/protocol-questions.md)
- [Timing semantic review](references/semantic-review.md)
- [Datasheet annotations](references/datasheet-annotations.md)
- [MCP tools](references/mcp-tools.md)
- [MCP registration](references/mcp-registration.md)
- [WaveDrom main repository](https://github.com/wavedrom/wavedrom)
- [WaveDrom tutorial](https://wavedrom.com/tutorial.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with WaveJSON/JSON5 source, rendered SVG by default, and optional PNG or self-contained HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns absolute artifact paths and states material timing assumptions; requires Node.js 20 or newer for bundled local scripts and MCP tools.]

## Skill Version(s):

0.3.1 (source: frontmatter, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
