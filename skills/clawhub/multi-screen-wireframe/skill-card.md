## Description:

Create or revise offline, AI-editable multi-screen wireframes and page-flow prototypes that open directly from local files without a build step.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ginuim](https://clawhub.ai/user/ginuim)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and design reviewers use this skill to generate or revise multi-screen wireframe prototypes for mobile apps, mini-program flows, desktop admin tools, and interactive product demos. It is intended for offline prototype delivery where agents should edit plain JavaScript screen files and users can review flows in a browser.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates or edits files in the output directory chosen by the user.

Mitigation: Use a deliberate output directory, review generated changes before adoption, and avoid pointing the workflow at unrelated project files.

Risk: Board settings and annotation drafts may be stored in the local browser while reviewing prototypes.

Mitigation: Sync annotations into source or export annotation JSON when needed, and clear browser storage for sensitive prototype sessions.

Risk: Validation scripts should not be run against untrusted prototype source without review.

Mitigation: Inspect prototype source first and run checks only on artifacts from trusted or reviewed sources.

## Reference(s):

- [Skill page](https://clawhub.ai/ginuim/skills/multi-screen-wireframe)
- [README](README.en.md)
- [User Guide](docs/user-guide.md)
- [Reference](reference.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Files, Shell commands, Configuration]

**Output Format:** [Offline prototype files with Markdown guidance and JavaScript/CSS source edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces browser-openable wireframe deliverables, source-edit prompts, annotations, and optional PNG or ZIP exports.]

## Skill Version(s):

2.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
