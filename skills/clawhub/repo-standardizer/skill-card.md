## Description:

Polish any GitHub repository's surface - labels, issue forms, PR template, CI workflows, CODEOWNERS, rulesets, and docs - while limiting changes to repository metadata and configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[programmingwtf](https://clawhub.ai/user/programmingwtf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to standardize new or existing GitHub repositories with labels, issue forms, pull request templates, CI workflows, CODEOWNERS, branch rules, and repository documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make GitHub repository configuration changes using the active authenticated account.

Mitigation: Confirm the exact OWNER/REPO, active GitHub account, and token scopes before applying changes; review the dry-run table before execution.

Risk: Branch rules, rulesets, workflow files, org repositories, overwrites, or deletion prompts can affect repository governance or CI behavior.

Mitigation: Require explicit confirmation for sensitive actions and verify the final applied, skipped, and failed checklist after changes are made.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/programmingwtf/skills/repo-standardizer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands plus repository configuration files and templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GitHub CLI and git; prompts for authentication, repository scope, language, automation posture, and confirmation before sensitive repository changes.]

## Skill Version(s):

0.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
