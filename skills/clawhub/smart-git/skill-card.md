## Description:

smart-git uses the smart-commit-host-agent CLI to help agents review local changes, create or review PRs/MRs, list open PRs/MRs, and batch-review PRs/MRs through an explicit Host-Agent turn loop.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yexinjia](https://clawhub.ai/user/yexinjia)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to route Git review and PR/MR tasks through a configurable CLI workflow while preserving explicit mode selection, token handling, and Host-Agent response steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can change repository state by committing, pushing, creating PRs/MRs, approving, merging, or publishing review output.

Mitigation: Review smart-commit.host-agent.json before live use, disable automatic actions that do not fit repository policy, and use dry-run behavior for reviews and batch reviews until the workflow is accepted.

Risk: Default PR/MR review behavior can automatically approve or merge changes after a passing review.

Mitigation: Set pullRequestReview.autoApprove and pullRequestReview.autoMerge to false unless automatic approval and merge are explicitly allowed for the target repository.

Risk: Create PR/MR mode can automatically stage, commit, push, and create a PR/MR after review.

Mitigation: Set git.autoCommit, git.autoPush, and pullRequestCreation.autoCreateAfterPush to false when teams require manual control over those steps.

## Reference(s):

- [Server-resolved source repository](https://github.com/yexinjia/smart-git)
- [ClawHub skill page](https://clawhub.ai/yexinjia/skills/smart-git)
- [smart-commit-host-agent package](https://www.npmjs.com/package/smart-commit-host-agent)
- [Configuration guide](CONFIG.md)
- [Setup guide](SETUP.md)
- [Host-Agent turn loop](HOST_AGENT_LOOP.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON turn-response content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can cause the agent to write Host-Agent response JSON files and run CLI commands that commit, push, create PRs/MRs, publish review comments, approve, or merge according to configuration.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
