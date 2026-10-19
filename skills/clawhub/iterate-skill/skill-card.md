## Description:

Automates multi-round code review and improvement, with a defensive mode for incremental coding tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers use Iterate to review and improve codebases across multiple quality dimensions, or to complete incremental coding tasks with defensive checks. A review-only mode produces findings without editing files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated edits and shell validation can change a repository or execute repository-provided scripts.

Mitigation: Review validation.commands and invariants.commands in iterate.config.yaml before use, and remove untrusted local scripts.

Risk: Automated git operations can affect branches or publish changes if enabled.

Mitigation: Use review-only mode for unfamiliar repositories and keep merge and push disabled unless intentionally enabled.

## Reference(s):

- [Iterate on ClawHub](https://clawhub.ai/jingzhao-l/skills/iterate-skill)

## Skill Output:

**Output Type(s):** [Code, Markdown, Configuration, Guidance]

**Output Format:** [Code changes, project configuration, and Markdown review reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review-only mode does not edit files.]

## Skill Version(s):

3.5.3 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
