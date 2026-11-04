## Description:

Builds deterministic lesson-plan skeletons from curriculum maps and checks existing plans for missing knowledge coverage, stages, sources, and time allocations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and curriculum teams use it to create structured lesson-plan drafts from their own curriculum maps and check plans for structural gaps. Developers can also run its deterministic checks in batch workflows or CI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing through npx may download and execute code beyond the files reviewed here.

Mitigation: Prefer reviewed local files or a verified, fixed package release.

Risk: Installation can overwrite customized skill files or existing template and output files.

Mitigation: Choose a specific agent or destination, preview installer paths with --dry-run, and back up customized files before overwriting them.

## Reference(s):

- [Curriculum map and structure format](references/map-format.md)
- [Lesson plan and check report format](references/plan-format.md)
- [Copyright and use boundaries](references/copyright.md)
- [Project homepage](https://github.com/YottaMeta/yotta-lesson)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-lesson)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Configuration]

**Output Format:** [Markdown lesson-plan skeletons and coverage reports, JSON plans and reports, and starter JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic outputs based on the supplied map, plan text, and optional structure configuration.]

## Skill Version(s):

0.1.3 (source: server release evidence, SKILL.md frontmatter, and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
