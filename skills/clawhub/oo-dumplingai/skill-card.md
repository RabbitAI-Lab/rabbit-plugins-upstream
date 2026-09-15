## Description:

DumplingAI lets an agent operate DumplingAI through an OOMOL-connected account to search catalog items, inspect account activity, and run DumplingAI capabilities or managed provider endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to interact with DumplingAI through the oo CLI, including catalog discovery, capability execution, usage review, transactions, balance, and budget checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that run scripts directly in a shell.

Mitigation: Do not let an agent run the remote installer automatically; install the oo CLI from a verified, versioned source with checksum or signature verification.

Risk: DumplingAI actions may execute service capabilities or provider endpoints with user-provided JSON input.

Mitigation: Inspect the live connector schema before constructing payloads and confirm the exact payload and expected effect before any write or destructive action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dumplingai)
- [DumplingAI homepage](https://www.dumplingai.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; requires user confirmation before write or destructive actions.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
