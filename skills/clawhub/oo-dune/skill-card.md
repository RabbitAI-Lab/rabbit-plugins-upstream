## Description:

Dune lets an agent operate Dune through an OOMOL-connected account to execute saved queries and retrieve query metadata, execution status, and result data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to inspect Dune queries, run saved query executions after confirmation, and retrieve execution status or result data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can execute a remote installer script for the oo CLI.

Mitigation: Review the installer before use and prefer a verified package or official installation process.

Risk: The execute_query action changes Dune state by starting a saved query execution.

Mitigation: Confirm the exact action payload and intended Dune account with the user before running write actions.

Risk: The skill operates through the Dune account connected to OOMOL.

Mitigation: Verify which account is connected and that the requested action matches the user's intended scope before sending payloads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-dune)
- [Dune Homepage](https://dune.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires oo CLI authentication and a connected Dune account; query execution should be confirmed before running.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
