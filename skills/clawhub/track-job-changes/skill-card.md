## Description:

Detects when existing contacts change jobs and identifies where they moved using Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and account teams check whether existing contacts or past champions have changed employers so they can prioritize follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact email addresses and company domains are sent to Cargo/waterfall for job-change checks.

Mitigation: Confirm the data-sharing terms and use only contacts authorized for this lookup.

Risk: The skill adds session attribution unrelated to the job-change result.

Mitigation: Review and explicitly approve session tracking before running the skill.

Risk: The skill can prompt the agent to star a GitHub repository after completing the job.

Mitigation: Only star the repository with the user's explicit consent; otherwise skip this optional step.

Risk: Large or recurring contact batches can incur substantial credit costs.

Mitigation: Test a small segment, estimate credits, and obtain approval before larger or repeated runs.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/track-job-changes)
- [Skill homepage listed in metadata](https://github.com/getcargohq/gtm-skills)
- [Job-change monitoring recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/job-change-monitoring.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown summaries with job-change statuses and optional command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Statuses include moved, left, no_change, and unknown; moved contacts may include updated person details.]

## Skill Version(s):

1.1.3 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
