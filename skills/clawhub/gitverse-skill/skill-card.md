## Description:

Own GitVerse (gitverse.ru) skill: repos, issues, PRs via REST API with a dependency-free Python CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[viknsagit](https://clawhub.ai/user/viknsagit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to manage GitVerse repositories, issues, and pull requests from an agent-accessible command-line workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a GitVerse token to read and modify repositories, issues, and pull requests.

Mitigation: Use a least-privilege token and install the skill only for workflows that require these GitVerse actions.

Risk: Changing GITVERSE_BASE_URL can route authenticated requests to a different endpoint.

Mitigation: Keep GITVERSE_BASE_URL unset unless a trusted HTTPS GitVerse-compatible endpoint is deliberately required.

Risk: The CLI can create issues and comments, close issues, and merge pull requests.

Mitigation: Confirm write, close, and merge actions with the user before execution, especially when actions are broad or irreversible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/viknsagit/skills/gitverse-skill)
- [GitVerse token settings](https://gitverse.ru/settings/tokens)
- [GitVerse API endpoint](https://api.gitverse.ru)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled CLI prints JSON responses from GitVerse API operations.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
