## Description:

Guides an agent through an end-to-end pull request flow that reviews the branch before publishing, pushes only with approval, creates provider-appropriate PRs, verifies settings, and reports PR URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to prepare, review, publish, create, and verify pull requests for single-repo or multi-repo work items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to push branches and create pull requests.

Mitigation: Require explicit user approval before any push and confirm the repo, branch, provider configuration, reviewers, auto-complete settings, and work-item links before proceeding.

Risk: Incorrect PR settings could misroute review or link the work to the wrong item.

Mitigation: Re-read each created PR and report verified reviewers, work-item links, auto-complete status, target branch, and PR URL.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown]

**Output Format:** [Markdown guidance with inline shell commands and PR summary tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user approval before pushing branches.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
