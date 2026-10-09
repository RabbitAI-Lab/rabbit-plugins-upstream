## Description:

Creates a local, deterministic lesson-plan skeleton from a curriculum map and checks existing plans for missing content, stages, sources, and time allocations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and curriculum teams use the skill to draft lesson-plan skeletons from their own curriculum maps and check existing plans for structural gaps. Developers can run its checks in CI; teachers remain responsible for instructional decisions and source verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation may target unintended directories or multiple agent environments.

Mitigation: Install a trusted pinned version; preview the target with --dry-run or --dir and use --global only when intended.

Risk: A structurally complete skeleton may be mistaken for a teacher-approved lesson or an authoritative curriculum interpretation.

Mitigation: Have a teacher review instructional choices and verify cited standards against official texts before use.

## Reference(s):

- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-lesson)
- [Publisher-listed project homepage](https://github.com/YottaMeta/yotta-lesson)
- [Curriculum map format](artifact/references/map-format.md)
- [Lesson plan and check report format](artifact/references/plan-format.md)
- [Copyright and usage boundaries](artifact/references/copyright.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lesson skeletons include sourced objectives and minute-level stages; checks report structural gaps and can trigger a CI gate.]

## Skill Version(s):

0.1.2 (source: frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
