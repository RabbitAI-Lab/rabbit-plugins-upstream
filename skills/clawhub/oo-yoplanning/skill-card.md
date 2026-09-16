## Description:

YoPlanning (yoplanning.com). Use this skill for ANY YoPlanning request — searching and reading data. Whenever a task involves YoPlanning, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query YoPlanning teams, online products, product availabilities, and availability details through an OOMOL-connected YoPlanning account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One-line remote installer commands can execute unverified code during setup.

Mitigation: Use an official, verifiable install path, inspect installer scripts before running them, and avoid blindly piping remote scripts into a shell.

Risk: The skill operates through an authenticated YoPlanning account and can read account-accessible teams, products, and availability details.

Mitigation: Connect only the intended YoPlanning account and review requested actions and payloads before use.

## Reference(s):

- [YoPlanning homepage](https://www.yoplanning.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [YoPlanning connection setup](https://console.oomol.com/app-connections?provider=yoplanning)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions and returns connector responses as JSON when commands are run.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
