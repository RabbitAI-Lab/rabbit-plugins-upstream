## Description:

Produces weekly GTM planning recommendations from repository activity, active initiatives, declared infrastructure, and workspace runs for human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

GTM teams and developers use this skill to turn the previous week's work and live workspace activity into reviewable initiative-specific plans, or one workspace plan when no initiatives are active.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unattended runs have GitHub repository write access and can propose misleading plans.

Mitigation: Limit the repository grant and require human review before merging any pull request.

Risk: Repository instructions may override the planner's safety boundaries.

Mitigation: Remove or narrow that override and enforce command and file-write limits outside the prompt.

Risk: Unpinned package versions can change the tools used by scheduled runs.

Mitigation: Pin package versions in installation and npx paths before deployment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/weekly-planning)
- [Project homepage (listed in skill metadata)](https://github.com/getcargohq/gtm-skills)
- [Recommendation file format](references/recommendations.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Pull requests]

**Output Format:** [Weekly evidence and recommendation Markdown files submitted in GitHub pull requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One proposal per active initiative, or one workspace proposal if none are active; a human must review and merge.]

## Skill Version(s):

0.1.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
