## Description:

Datalust Seq (datalust.co) skill for reading, searching, querying, ingesting, creating, updating, and deleting Seq events, signals, and saved queries through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Datalust Seq data and configuration through the oo CLI, including event search, query execution, event ingestion, and saved query or signal administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer execution from the network.

Mitigation: Review the installer path before use and prefer a verified, versioned, signed source or inspect the downloaded installer before running it.

Risk: Write, ingest, update, or delete actions can change or remove Seq data visible to the connected account.

Mitigation: Confirm the exact payload, target, and expected effect before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-datalust)
- [Datalust Seq homepage](https://datalust.co/seq)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke oo CLI actions that return structured JSON responses.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
