## Description:

StateRoot is a bootstrap skill that installs and sets up the StateRoot CLI so AI coding agents can share persona, memory, plans, skills, sessions, and project history across supported harnesses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[usama04](https://clawhub.ai/user/usama04)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this bootstrap skill when StateRoot is not installed or has not yet been set up on a machine. It guides installation from official release assets and one-time setup so supported coding-agent harnesses can use StateRoot's built-in continuity workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: StateRoot setup persistently changes local agent harness configuration across tools.

Mitigation: Review the dry-run output before setup and proceed only when persistent harness hooks are desired.

Risk: Non-interactive setup accepts defaults that may not match the user's intended harness configuration.

Mitigation: Prefer interactive setup when possible, and use non-interactive setup only when the user is comfortable accepting defaults.

Risk: Installing through remote release assets executes local installer code.

Mitigation: Use only the documented official release assets, ask before piping an installer to a shell, and fail closed on checksum or installer errors.

## Reference(s):

- [StateRoot homepage](https://stateroot.dev)
- [Installation documentation](https://stateroot.dev/docs/getting-started/installation)
- [Setup documentation](https://stateroot.dev/docs/getting-started/setup)
- [Privacy documentation](https://stateroot.dev/docs/guides/privacy)
- [FAQ](https://stateroot.dev/docs/reference/faq)
- [GitHub releases](https://github.com/CognizTech/stateroot/releases)
- [Disclosure](references/disclosure.md)
- [Install](references/install.md)
- [Bootstrap failures](references/failures.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bootstrap guidance only; the skill should expire after StateRoot setup succeeds.]

## Skill Version(s):

1.1.1 (source: server release evidence and skill.manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
