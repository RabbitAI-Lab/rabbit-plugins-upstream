## Description:

Provides a four-stage pre-install security review of agent skills, combining source, code, permissions, and risk checks with a lightweight checker and a report for human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to assess an unfamiliar agent skill before installation and record findings for a human installation decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing into unintended agent directories, especially with bulk installation.

Mitigation: Specify --agent or --dir and use -g only when installation across multiple agents is intended.

Risk: An unpinned npx installation could retrieve a changed package version.

Mitigation: Pin the npm package version before running npx.

Risk: Scanning an overly broad directory may expose unrelated local files to the checker.

Mitigation: Point the checker at the specific skill directory under review, not a whole home or workspace directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-vetter)
- [Project homepage (listed in ClawHub metadata; import provenance unavailable)](https://github.com/YottaMeta/yotta-vetter)
- [Four-stage vetting checklist](references/checklist.md)
- [Vetting report template](references/vetting-report-template.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Shell commands]

**Output Format:** [Markdown vetting report or JSON findings, with optional deep-scan command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk levels and suggested decisions require human confirmation.]

## Skill Version(s):

0.2.6 (source: skill frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
