## Description:

SatisMeter (satismeter.com). Use this skill for SatisMeter requests that search, read, and inspect project, survey, statistics, and response data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to retrieve SatisMeter project, survey, survey statistics, and response data through the oo CLI after the account is connected. It is suited for read-oriented customer feedback analysis and reporting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes commands that pipe remote installer scripts directly into a shell.

Mitigation: Use a verified package or download and inspect the installer before execution; only run installation commands in an environment where that risk is acceptable.

Risk: SatisMeter access is mediated through OOMOL and requires an account connection.

Mitigation: Connect only the intended SatisMeter account, review requested scopes, and run only the actions and payloads the user explicitly intends.

Risk: Connector actions depend on live schemas and may fail or behave unexpectedly if payloads are guessed.

Mitigation: Inspect the action schema before every run and build JSON payloads from the returned contract.

## Reference(s):

- [ClawHub SatisMeter skill page](https://clawhub.ai/oomol/skills/oo-satismeter)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [SatisMeter homepage](https://satismeter.com)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON responses from the oo connector, including data and execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
