## Description:

Summarize all outstanding work not merged into main/default branch (including unmerged branches, open PRs, uncommitted changes, and stashes).

This skill is ready for commercial/non-commercial use.

## Publisher:

[homostellaris](https://clawhub.ai/user/homostellaris)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to have an agent audit a Git repository for outstanding unmerged work, including local changes, stashes, open pull requests, branch divergence, and next-step recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may inspect local Git state, stashes, branch history, diff summaries, and GitHub pull request metadata.

Mitigation: Use the skill only in repositories where that local and GitHub repository information is appropriate for the agent to review.

Risk: Running a remote fetch can update local remote-tracking references.

Mitigation: Use the workflow interactively and confirm before allowing a fetch that changes local remote-tracking state.

Risk: Offline or unauthenticated environments can produce a report based on cached local state rather than current remote pull request data.

Mitigation: Clearly state in the generated report when results are based on cached or local state.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/homostellaris/skills/summarize-outstanding-work)
- [Server-resolved GitHub provenance](https://github.com/homostellaris/dotfiles/tree/master/agents/skills/summarize-outstanding-work)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with repository status sections, tables, command-derived summaries, and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May note when results are based on cached or local repository state.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
