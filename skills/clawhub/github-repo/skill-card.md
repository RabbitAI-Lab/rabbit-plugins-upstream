## Description:

GitHub Repo helps agents configure and verify GitHub repositories, including Actions workflows, Dependabot, templates, CODEOWNERS, branch protection, CodeRabbit, and Copilot setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to prepare GitHub repositories for collaborative development, CI workflows, dependency automation, review integrations, templates, ownership files, branch protection, and repository readiness checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Helm Chart GitHub Pages workflow template can publish from the repository root, which may expose unintended repository files.

Mitigation: Before committing generated workflow files, change the template to publish only a clean chart artifact directory.

Risk: Default CodeRabbit and Copilot configuration choices may not match a repository's language, visibility, seat, or policy requirements.

Mitigation: Confirm repository policy and service availability before applying those configuration files.

Risk: Generated workflow, dependency automation, template, and branch protection changes can materially change CI, release, and collaboration behavior.

Mitigation: Review generated diffs, verify workflow commands locally where possible, and confirm branch protection API payloads before applying them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/github-repo)
- [Actions workflow guide](artifact/actions.md)
- [Repository setup guide](artifact/setup.md)
- [Repository verification guide](artifact/verify.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with YAML, shell command, and GitHub API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or write repository configuration files, GitHub Actions workflow files, Dependabot configuration, templates, CODEOWNERS, and branch protection API payloads.]

## Skill Version(s):

0.2.1 (source: server release metadata and changelog, released 2026-09-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
