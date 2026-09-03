## Description:

Pushes all branches in a stack and opens or updates one dependent PR per slice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill after creating a stacked branch topology to push slice branches, create or update dependent draft GitHub pull requests, and post a stack summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can push branches and create or update GitHub pull requests in the current repository.

Mitigation: Review the branch prefix, base branch, and generated PR text before allowing the commands to run.

Risk: Generated PR titles, bodies, and stack summaries may need human correction before publication.

Mitigation: Keep PRs as drafts until each slice has been reviewed and the PR text is ready.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-stack-push)
- [Sanctum plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes Git and GitHub CLI command sequences for stack branch publication and draft PR creation.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter says 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
