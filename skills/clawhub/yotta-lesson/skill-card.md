## Description:

yotta-lesson builds deterministic lesson-plan skeletons from curriculum maps and checks existing lesson plans for missing knowledge points, stages, sources, time annotations, and total-minute mismatches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers, curriculum teams, and automation developers use this skill to create reproducible lesson-plan skeletons from school-provided curriculum maps and to check lesson-plan structure in batch or CI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer options can persistently copy the skill into multiple agent environments.

Mitigation: Install to a narrow target such as --agent codex or an explicit --dir, and avoid -g unless broad installation is intended.

Risk: Unpinned npx or source installs may install code that differs from the reviewed release.

Mitigation: Prefer a pinned package version or a reviewed tagged source, and check for an existing yotta-lesson directory before installing.

Risk: Lesson skeletons and coverage findings are preparation aids and may not satisfy local curriculum or school policy without review.

Mitigation: Have teachers verify knowledge wording, source labels, timing, and school-specific requirements before publishing or using a plan.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-lesson)
- [Project homepage](https://github.com/YottaMeta/yotta-lesson)
- [Curriculum map and structure format](references/map-format.md)
- [Lesson skeleton and check report contract](references/plan-format.md)
- [Copyright and usage boundaries](references/copyright.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON lesson skeletons, JSON findings reports, and command guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic local output; generated_at is the primary run-varying field.]

## Skill Version(s):

0.1.0 (source: frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
