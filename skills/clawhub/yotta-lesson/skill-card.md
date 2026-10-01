## Description:

Creates a locally generated lesson-plan skeleton from a curriculum map and checks existing plans for missing content, stages, citations, and timing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and curriculum teams use this skill to draft lesson-plan outlines from their own curriculum maps and check existing plans for structural gaps before review or CI submission. Teachers remain responsible for the final instructional design and verifying curriculum citations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the skill into agent skill directories changes what agents can use in future sessions.

Mitigation: Choose a specific --agent or --dir target rather than --global, and pin the package version when installing via npx.

Risk: A structural coverage check does not establish that curriculum citations or teaching choices are correct.

Mitigation: Have a teacher review the lesson design and verify citations against official curriculum texts.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-lesson)
- [Project homepage (listed in skill metadata; import provenance unavailable)](https://github.com/YottaMeta/yotta-lesson)
- [Curriculum map format](references/map-format.md)
- [Lesson plan and gap report format](references/plan-format.md)
- [Copyright and usage boundaries](references/copyright.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON lesson-plan skeleton and coverage findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local, deterministic checks with an optional CI findings threshold.]

## Skill Version(s):

0.1.1 (source: ClawHub release, skill frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
