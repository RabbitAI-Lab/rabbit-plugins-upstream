## Description:

AutoGitHub helps agents manage GitHub repositories through repository operations, pull request review, changelog generation, issue and project workflows, and GitHub Actions CI/CD setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shiiyyo](https://clawhub.ai/user/shiiyyo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to automate common GitHub repository maintenance tasks, including PR inspection, changelog creation, issue handling, project reporting, and generation of CI/CD workflow files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate with powerful GitHub repository credentials.

Mitigation: Use a fine-grained personal access token limited to the specific repositories and permissions required.

Risk: The configuration file may store sensitive GitHub token material.

Mitigation: Avoid committing configuration files, protect or avoid plaintext local token storage, and do not pass secrets through shell history.

Risk: Generated CI/CD workflows can affect build, package, and deployment behavior.

Mitigation: Review generated workflows before committing them and fix the scanner-reported command-injection and mutable-action template issues before CI/CD or production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shiiyyo/skills/github-manager)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)
- [config-template.json](artifact/config-template.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON configuration, and generated workflow/code files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local GitHub configuration and GitHub Actions workflow files for review before committing.]

## Skill Version(s):

1.0.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
