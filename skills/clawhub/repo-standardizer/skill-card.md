## Description:

Polishes GitHub repository metadata and configuration, including labels, issue forms, PR templates, CI workflows, CODEOWNERS, rulesets, and docs, without changing application code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[programmingwtf](https://clawhub.ai/user/programmingwtf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to standardize new or existing GitHub repositories by auditing repository setup, proposing a dry-run plan, and applying metadata, workflow, governance, and documentation updates after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make real GitHub repository metadata and configuration changes, including CI workflows, branch rulesets, labels, commits, and pushes.

Mitigation: Review the dry-run plan and confirmation prompts before applying changes, especially for private or organization repositories, branch rulesets, CI workflow files, label deletion, and operations that commit and push.

Risk: The skill requires authenticated GitHub access and may use tokens with repository, workflow, or organization scopes.

Mitigation: Verify the acting GitHub account before use, avoid sharing tokens in chat or logs, and use only the minimum scopes required for the target repository.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/programmingwtf/skills/repo-standardizer)
- [Skill definition](artifact/SKILL.md)
- [Template catalog](artifact/templates/)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated repository configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify GitHub repository metadata and configuration after user confirmation.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
