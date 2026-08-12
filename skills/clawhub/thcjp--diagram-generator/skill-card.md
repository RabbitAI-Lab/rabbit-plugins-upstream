## Description:

Generates and edits Draw.io, Mermaid, and Excalidraw diagrams from natural-language intent using structured JSON specifications for network topology, architecture, flowchart, swimlane, UML, and whiteboard use cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical writers, and automation teams use this skill to turn prompts or structured inputs into diagram specs and generated Draw.io, Mermaid, or Excalidraw files for architecture documentation, network topology planning, process modeling, UML, and whiteboard-style collaboration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to run an external connector package and may write or overwrite diagram files.

Mitigation: Review connector configuration before use, pin or verify the package source where possible, and use a dedicated workspace and output directory.

Risk: Diagram content and callback URLs may be sent through connector workflows.

Mitigation: Do not provide sensitive diagram content or callback URLs unless the destination is trusted and approved.

Risk: The security scan says some instructions under-disclose execution and file-write powers.

Mitigation: Confirm required tools and expected filesystem changes before installing or invoking the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/diagram-generator)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with JSON diagram specifications, connector commands, and generated diagram file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or overwrite Draw.io, Mermaid, or Excalidraw files through an external connector.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter reports 1.1.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
