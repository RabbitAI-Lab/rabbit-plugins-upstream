## Description:

Ingest Tencent Meeting recordings, minutes, and transcripts into the Research KB by delegating platform fetching to tencent-meeting-skill, then letting OpenClaw generate structured meeting wiki pages and related KB updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[myd2002](https://clawhub.ai/user/myd2002)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research teams use this skill to ingest Tencent Meeting recordings, minutes, and transcripts into a Gitea-backed Research KB. It prepares bounded meeting context for OpenClaw, validates Markdown drafts and compact manifests, and applies meeting-derived KB updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting transcripts and minutes may contain sensitive project or personal information.

Mitigation: Install only where archiving meeting material into the intended Gitea KB is approved, and review repository access controls before deployment.

Risk: A broadly scoped Gitea bot token could write outside the intended knowledge base.

Mitigation: Limit GITEA_BOT_TOKEN to the intended KB repository and required write operations.

Risk: An untrusted Tencent Meeting command could fetch or transform meeting material unexpectedly.

Mitigation: Use a trusted installed tencent-meeting-skill or tencent-meeting-mcp command, and control TENCENT_MEETING_SKILL_COMMAND in the runtime environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/myd2002/skills/tencent-meeting-ingest)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown drafts, compact JSON manifests, JSON result envelopes, and command-line workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Archives source meeting materials, updates Gitea KB pages, catalog.json, index.md, and incremental scan snapshots.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
