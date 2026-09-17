## Description:

DumplingAI (dumplingai.com). Use this skill for DumplingAI requests involving search, catalog inspection, account visibility, and running DumplingAI capabilities through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate DumplingAI through an OOMOL-connected account, including discovering catalog items, checking account usage, and running DumplingAI capabilities or managed provider endpoints with JSON input.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can execute an internet-hosted installer for the oo CLI.

Mitigation: Only run installer commands after a matching setup failure, and verify OOMOL's installer source and installation method before execution.

## Reference(s):

- [ClawHub DumplingAI Skill](https://clawhub.ai/oomol/skills/oo-dumplingai)
- [DumplingAI Homepage](https://www.dumplingai.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; connector responses include data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
