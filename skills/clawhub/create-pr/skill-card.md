## Description:

Guides an agent through a gated pull-request publication workflow that reviews the branch, asks for approval before pushing, creates provider-specific PRs, verifies PR settings, and reports the resulting URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to publish ready branches as pull requests with a review gate, explicit push approval, provider-specific defaults, multi-repository coordination, and post-creation verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A branch could be pushed or a PR could be opened against the wrong repository or target branch.

Mitigation: Confirm the work item, branch, touched repositories, configured target branch, and repository configuration before publication.

Risk: Publishing code can expose changes before the user is ready.

Mitigation: Require explicit user approval before running the branch push.

Risk: PR settings such as required reviewers, work-item links, auto-complete, or target branch can be missing or incorrect after creation.

Mitigation: Re-read each PR after creation and report the verified settings and URL.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/create-pr)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown status summaries with shell commands, quoted verification results, PR descriptions, and PR URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill requires user approval before pushing branches and expects verification of PR settings after creation.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
