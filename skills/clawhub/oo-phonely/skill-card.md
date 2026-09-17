## Description:

Phonely enables agents to search and read Phonely agents, calls, summaries, and transcripts through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Phonely connector schemas and retrieve accessible Phonely agents, calls, summaries, and transcripts through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes direct execution of remote installer scripts.

Mitigation: Install the oo CLI from a verified release or package manager when possible, validate checksums or signatures, and avoid running installer pipelines from an elevated shell.

Risk: Read operations can return Phonely call summaries and transcripts available to the connected account.

Mitigation: Run actions only for user-requested agents or calls and avoid exposing returned call data beyond the intended conversation or workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-phonely)
- [Phonely Homepage](https://www.phonely.ai/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown text with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses include data and meta.executionId; listed Phonely actions are read-only.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
