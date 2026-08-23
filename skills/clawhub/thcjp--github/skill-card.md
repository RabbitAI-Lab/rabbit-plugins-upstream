## Description:

GitHub开发工具 helps agents use the GitHub gh CLI to manage repositories, issues, pull requests, workflow runs, API calls, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to have an agent operate GitHub through the gh CLI for repository workflow tasks such as issue management, pull request creation, CI/CD run handling, API calls, and webhook setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives agents broad GitHub command and API authority through gh CLI.

Mitigation: Review repository targets, branches, API paths, workflow runs, and webhook URLs before allowing commands that create or modify GitHub resources.

Risk: GitHub operations may change issues, pull requests, CI/CD runs, API resources, or webhooks.

Mitigation: Use the skill only in repositories and organizations where the agent has appropriate permissions and the intended action has been confirmed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/github)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce GitHub operation results, status changes, execution logs, and follow-up guidance.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
