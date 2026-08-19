## Description:

A zero-dependency, plug-and-play skill for adding interactive PRD pin annotations, multi-version requirement management, visual tables, Mermaid diagrams, and full PRD document views to local HTML prototypes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[barry0-0](https://clawhub.ai/user/barry0-0)

### License/Terms of Use:

MIT-0

## Use Case:

Product managers, designers, and prototype-building agents use this skill to add in-place PRD annotations to static HTML prototypes, manage requirement versions, and generate shareable PRD views or exports. It is intended for trusted local prototype projects where generated files can be reviewed before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local save server can write project files with weak access controls.

Mitigation: Run it only for trusted local prototype projects, bind it to 127.0.0.1, add request controls, and sanitize page filenames before real use.

Risk: Imported PRD files are rendered into the prototype UI.

Mitigation: Review imported PRD files before loading them and only import content from trusted project collaborators.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/barry0-0/skills/pm-proto-prd-pin)
- [Artifact README](artifact/README.md)
- [Artifact Skill Definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown-style agent guidance with code snippets, shell commands, and file-change instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local prototype files, JavaScript PRD data files, and exportable PRD Markdown or JS data when applied by an agent.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
