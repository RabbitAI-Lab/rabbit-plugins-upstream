## Description:

A file-based memory manager that helps agents store, search, rank, pin, decay, and export conversational memories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[147258xuan](https://clawhub.ai/user/147258xuan)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents can use Supermemory to retain useful conversational facts across sessions, retrieve them by query, and manage what remains over time. It supports pinning important entries and exporting memory data as JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports shell-command injection risk.

Mitigation: Prevent untrusted input from reaching shell commands and review commands before running them.

Risk: Stored secrets or memories may be handled unsafely, and the memory store may receive unintended writes.

Mitigation: Avoid storing raw credentials and protect the memory store from unintended writes.

Risk: The security scan is incomplete: one component was only partially inspected and a tool-misuse analyzer was degraded.

Mitigation: Review flagged behavior and the partially inspected component before deployment.

## Reference(s):

- [Supermemory on ClawHub](https://clawhub.ai/147258xuan/skills/supermemory)

## Skill Output:

**Output Type(s):** [Text, JSON files, Guidance]

**Output Format:** [JSON memory records and text search or statistics results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores memory nodes and indexes in local files; supports ranked retrieval, decay, pinning, and JSON export.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
