## Description:

Interact with GitHub using the `gh` CLI for issues, pull requests, CI runs, logs, and advanced API queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to have an agent operate GitHub through the `gh` CLI for repository issues, pull requests, workflow runs, logs, and custom API queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated `gh` commands may act through the user's authenticated GitHub account and modify repository resources.

Mitigation: Review commands before execution, especially commands affecting issues, pull requests, workflow runs, or repository settings.

Risk: Repository selection mistakes can direct reads or actions at the wrong GitHub repository.

Mitigation: Check explicit `--repo owner/repo` arguments or URLs before running suggested commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/eohmig/skills/github)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include GitHub CLI JSON output and jq filtering examples.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
