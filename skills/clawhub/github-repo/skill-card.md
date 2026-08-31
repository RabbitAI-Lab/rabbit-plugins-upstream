## Description:

GitHub Repo helps agents configure, verify, and maintain GitHub repository workflows, integrations, templates, ownership files, branch protection, and prerequisite checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to generate GitHub Actions and Dependabot configuration, set up repository collaboration files, configure supported integrations, and verify that a repository is ready for a GitHub-flow workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated workflows, templates, or integration files may conflict with existing repository conventions or governance rules.

Mitigation: Review proposed file changes before accepting them, especially where the repository already has workflow, template, CODEOWNERS, or integration configuration.

Risk: Branch protection updates can alter existing repository policy if applied without preserving current settings.

Mitigation: Read existing branch protection first, normalize the returned settings, merge requested changes, and confirm the final payload before applying it.

Risk: Workflow templates may need current action versions, project-specific install steps, or local command verification before use.

Mitigation: Verify referenced action versions and run the workflow commands locally before committing generated workflow files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/github-repo)
- [Actions guide](artifact/actions.md)
- [Setup guide](artifact/setup.md)
- [Verification guide](artifact/verify.md)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with YAML, Markdown, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or write repository configuration files and GitHub branch protection changes when selected by the user.]

## Skill Version(s):

0.2.0 (source: server release metadata and CHANGELOG, released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
