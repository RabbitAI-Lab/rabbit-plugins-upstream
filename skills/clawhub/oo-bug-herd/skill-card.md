## Description:

BugHerd helps agents inspect schemas and operate BugHerd projects, tasks, comments, attachments, and organization details through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support teams use this skill to read BugHerd data and, after confirmation, create or update projects, tasks, comments, and URL-based attachments through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance includes remote installer commands that download and execute scripts without verification.

Mitigation: Review the OOMOL CLI installation path first; prefer an official package manager or a pinned installer with checksum or signature verification.

Risk: Write actions can create or update BugHerd projects, tasks, comments, and attachments.

Mitigation: Confirm the exact BugHerd project, task, action, and payload before running write actions.

## Reference(s):

- [BugHerd homepage](https://bugherd.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-bug-herd)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects containing data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.3 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
