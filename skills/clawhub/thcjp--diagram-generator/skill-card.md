## Description:

Generates and edits Draw.io, Mermaid, and Excalidraw diagrams from natural-language diagram requests and structured diagram specifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and documentation teams use this skill to create or update architecture, topology, flowchart, swimlane, UML, and whiteboard-style diagrams for repositories, reviews, and workflow documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary flags broad execution, generic API key usage, and unpinned runtime package setup.

Mitigation: Review connector configuration before installation, prefer a pinned known-good connector package or local path, and use narrowly scoped secrets instead of a generic API_KEY.

Risk: Diagram generation can write files to configured output paths and may overwrite existing work if paths are reused.

Mitigation: Use project-local output directories and confirm target filenames or paths before allowing existing files to be overwritten.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/diagram-generator)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON diagram specifications, connector calls, and generated diagram file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Draw.io, Mermaid, or Excalidraw diagram artifacts through a configured diagram connector.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter reports 1.1.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
