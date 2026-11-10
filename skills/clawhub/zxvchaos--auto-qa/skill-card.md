## Description:

Auto Qa runs web QA flows in OpenClaw, captures screenshots, console, network, and trace evidence, and produces reports and repair prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zxvchaos](https://clawhub.ai/user/zxvchaos)

### License/Terms of Use:


## Use Case:

Developers and QA engineers use this skill to run browser-based smoke and regression checks against web applications, collect execution evidence, and turn failures into release reports and repair task packages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser QA evidence can include screenshots, console logs, network records, and traces that expose sensitive page data.

Mitigation: Run against non-sensitive pages when possible, review captured evidence before sharing, and avoid sensitive authenticated pages unless sharing behavior has been reviewed.

Risk: Report screenshots may be sent automatically to an inferred recent OpenClaw chat session.

Mitigation: Use explicit notification targets or disable auto-current notification before testing sensitive pages.

Risk: Default orphan-process cleanup can terminate other OpenClaw browser processes in shared or concurrent environments.

Mitigation: Disable orphan-process cleanup or isolate the browser profile when other users or concurrent runs may share the host.

## Reference(s):

- [AutoQA status snapshot](references/state_snapshot_20260220.md)
- [Auto Qa ClawHub release](https://clawhub.ai/zxvchaos/skills/auto-qa)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands plus generated JSON, HTML, screenshot, trace, and prompt files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces browser QA evidence, release-decision summaries, fix plans, and next-window repair prompts.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
