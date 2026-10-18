## Description:

Ranks the previous week's go-to-market activity against active initiatives and live workspace activity, then proposes next steps in reviewable pull requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales leaders and revenue operations teams use this skill to review the previous week's initiatives, repository activity, and workspace runs, then propose the next week's work for human approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository instructions can override the planner's safety and review rules during an unattended run.

Mitigation: Allow repository instructions to guide style only; keep safety, command, file-scope, and review rules higher priority.

Risk: Unpinned CLI and runtime tooling can change the behavior of scheduled runs.

Mitigation: Pin the Cargo CLI and tsx versions through a lockfile before deployment.

Risk: Write-capable repository credentials could allow changes outside the intended review flow.

Mitigation: Use read-only Cargo credentials and restrict GitHub permissions to dedicated branches and pull requests, without merge or default-branch push access.

## Reference(s):

- [Weekly Planning on ClawHub](https://clawhub.ai/cargo-ai/skills/weekly-planning)
- [Cargo GTM skills project](https://github.com/getcargohq/gtm-skills)
- [Recommendation file format](references/recommendations.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Configuration guidance]

**Output Format:** [Markdown planning files and reviewable pull requests, with setup guidance and project configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One pull request per active initiative, or one workspace pull request when none are active; a human reviews and merges. Live deployment has not been verified.]

## Skill Version(s):

0.1.2 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
