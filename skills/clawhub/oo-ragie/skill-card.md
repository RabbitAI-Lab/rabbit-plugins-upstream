## Description:

Ragie provides agent access to read, create, update, retrieve, and delete Ragie data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Ragie documents, partitions, connections, metadata, summaries, and semantic retrieval from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can run remote installer scripts on the user's machine.

Mitigation: Review the installer URL and prefer a pinned, signed, or checksum-verified oo CLI release before approving setup.

Risk: Write and destructive Ragie actions can modify or remove documents, partitions, metadata, limits, or connection state.

Mitigation: Confirm the exact action, target, and JSON payload with the user before running write or destructive commands.

## Reference(s):

- [Ragie homepage](https://www.ragie.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ragie)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions may produce JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
