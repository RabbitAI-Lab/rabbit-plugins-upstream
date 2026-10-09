## Description:

Turns the previous week's GTM activity, initiatives, and workspace runs into reviewable weekly planning recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales leaders and revenue operations teams use this skill to compare last week's GTM activity with active initiatives and live runs, then review proposed next steps in pull requests before merging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A scheduled agent has repository write access and broad command authority, with important boundaries expressed mainly in instructions.

Mitigation: Enforce allowed commands and repository write paths outside the agent instructions; review the planned diff and first scheduled run before deployment.

Risk: Installing an unpinned CLI version or granting access to a sensitive Cargo workspace may expose additional capabilities or data.

Mitigation: Pin tool versions and review workspace access before installation.

## Reference(s):

- [Project homepage](https://github.com/getcargohq/gtm-skills)
- [Recommendation guidance](references/recommendations.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown evidence snapshots and recommendation files delivered in reviewable pull requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One pull request per active initiative, or one workspace pull request if none; a human reviews and merges.]

## Skill Version(s):

0.1.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
