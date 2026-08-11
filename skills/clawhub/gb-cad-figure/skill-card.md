## Description:

Generates GB/T-style engineering drawing workflows and CAD outputs for agents, including drawing frames, title blocks, dimensions, isometric solids, PDF/DXF generation, and optional DWG conversion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hegenerkondo335-dot](https://clawhub.ai/user/hegenerkondo335-dot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to generate standards-oriented CAD drawing scripts and deliver PDF, DXF, and optionally DWG files for mechanical or architectural drafting tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The DWG workflow can download and execute a third-party ODA File Converter AppImage during conversion.

Mitigation: Generate PDF/DXF only when DWG is not required, or manually provide a trusted converter binary and review its source and hash before running conversion.

Risk: Included examples and CAD-generation scripts write local drawing outputs and may be unsuitable for shared workspaces without review.

Mitigation: Run the skill in an isolated workspace, review output paths before execution, and avoid running example scripts unchanged in shared environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hegenerkondo335-dot/skills/gb-cad-figure)
- [Publisher profile](https://clawhub.ai/user/hegenerkondo335-dot)
- [artifact/README.md](artifact/README.md)
- [artifact/SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with Python and shell command snippets; generated artifacts may include PDF, DXF, and DWG files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [DWG conversion is optional and depends on a local ODA File Converter workflow; PDF and DXF generation use local Python scripts.]

## Skill Version(s):

1.2.4 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
