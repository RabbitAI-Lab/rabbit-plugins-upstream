## Description:

Creates or revises complete offline multi-screen wireframes and page-flow prototypes with Vue 3 Global Build, multi-file JavaScript screens, no build step, no Node dependency in the deliverable, and direct file:// opening.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ginuim](https://clawhub.ai/user/ginuim)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and product teams use this skill to generate and revise offline, AI-editable multi-screen wireframe prototypes for mobile apps, mini-program flows, desktop admin tools, interactive demos, and visual-reference reconstruction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated prototypes are local executable browser files and may include generated JavaScript.

Mitigation: Review generated prototype source before sharing or running it, and keep mock data separate from real credentials or secrets.

Risk: Optional Node validation scripts inspect prototype projects selected by the user.

Mitigation: Run validation only against prototype directories that the user intends to trust or edit.

Risk: Wireframe screens can display static or sanitized HTML through Vue Global features.

Mitigation: Use text interpolation for uncertain content and avoid binding user input, URL parameters, local storage, or external API data into rendered HTML.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ginuim/skills/multi-screen-wireframe)
- [README](README.md)
- [Usage Guide](docs/使用说明.md)
- [Technical Reference](reference.md)
- [Component Contract](starter/COMPONENTS.md)

## Skill Output:

**Output Type(s):** [Code, Files, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Offline HTML, CSS, and JavaScript prototype files with Markdown guidance and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces file://-openable Vue Global wireframe projects with editable source screens, annotations, and export support.]

## Skill Version(s):

2.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
