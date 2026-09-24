## Description:

Visual Interactive Courseware helps agents turn curriculum topics into self-contained interactive HTML courseware with SVG visuals, knowledge notes, teacher guidance, and audit checks across subjects such as biology, history, geography, physics, chemistry, and mathematics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erich1566](https://clawhub.ai/user/erich1566)

### License/Terms of Use:

MIT-0

## Use Case:

Educators, curriculum developers, and agent users use this skill to research a lesson topic, map it into interactive scenes, generate offline browser-ready courseware, and produce supporting knowledge and teacher materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary flags an instruction to remove AI image watermarks, which can weaken provenance and rights signals.

Mitigation: Use only licensed or self-created images, preserve provenance and safety markings, and regenerate clean assets or use authorized source files instead of removing watermarks.

Risk: Generated lesson visuals and explanations can be inaccurate for the target curriculum, learner level, or subject matter.

Mitigation: Validate key terms, diagrams, numerical claims, and AI-generated science imagery against authoritative curriculum or domain sources before classroom use.

Risk: Interactive HTML courseware may fail offline, accessibility, readability, or classroom display requirements if it is not checked before delivery.

Mitigation: Run the bundled audit script, browser screenshot review, and functional regression checks before delivery.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/erich1566/skills/visual-interactive-courseware)
- [Workflow Reference](artifact/references/workflow.md)
- [Design Guide](artifact/references/design-guide.md)
- [Audience Matrix](artifact/references/audience-matrix.md)
- [Subject Examples](artifact/references/subject-examples.md)
- [Courseware Template](artifact/assets/template.html)
- [Courseware Audit Script](artifact/scripts/audit_courseware.py)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance plus generated self-contained HTML, CSS, JavaScript, SVG, and audit reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project files such as knowledge integration notes, reference SVG assets, a single-file courseware HTML document, teacher notes, and audit output.]

## Skill Version(s):

1.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
