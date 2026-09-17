## Description:

Datalust Seq (datalust.co). Use this skill for Datalust Seq requests that read, create, update, delete, search, query, and ingest Seq data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Datalust Seq data through the OOMOL `oo` CLI, including event search, SQL-style queries, saved queries, signals, and event ingestion. The skill can perform state-changing and destructive actions when the user confirms the exact payload and target.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup instructions can execute unverified code.

Mitigation: Prefer a signed or package-manager installation path, verify checksums or signatures when available, and avoid running remote installer scripts in an elevated shell.

Risk: Write and destructive actions can change or remove Datalust Seq resources.

Mitigation: Review the exact payload, target identifier, and expected effect before approving write actions; require explicit approval before destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-datalust)
- [Datalust Seq homepage](https://datalust.co/seq)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return structured JSON from Datalust Seq connector actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
