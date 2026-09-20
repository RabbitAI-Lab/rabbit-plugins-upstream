## Description:

Datalust Seq helps agents operate a user's OOMOL-connected Datalust Seq account for event search, saved queries, signals, and structured log ingestion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to query Seq events, manage saved queries and signals, and ingest structured log events from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts in a shell.

Mitigation: Review the oo CLI installation path first; prefer official, version-pinned installers with checksum or signature verification, and do not allow the agent to run curl-to-bash or irm-to-iex setup commands automatically.

Risk: Write and destructive actions can change or delete Datalust Seq resources.

Mitigation: Confirm the exact target, payload, and expected effect before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [Datalust Seq homepage](https://datalust.co/seq)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Datalust connection setup](https://console.oomol.com/app-connections?provider=datalust)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-datalust)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill asks the agent to inspect live connector schemas before building action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence release.version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
