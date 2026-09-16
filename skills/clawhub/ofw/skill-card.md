## Description:

This skill guides agents working with OurFamilyWizard (OFW) co-parenting messages, calendar events, expenses, journal entries, drafts, and related account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to retrieve and manage OFW co-parenting records, including messages, calendar entries, shared expenses, and journal entries. It also guides higher-impact workflows such as drafting, sending, deleting, marking messages read, uploading attachments, and checking current server state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables authenticated access to sensitive OFW family and legal records, including write operations.

Mitigation: Install and use it only after review, with explicit user confirmation before sends, deletions, mark-as-read actions, or changes to public or legal records.

Risk: The setup flow can run mutable external package code.

Mitigation: Prefer a pinned, reviewed package version or commit and avoid global installs where possible.

Risk: The setup examples place OFW credentials in environment configuration that may be stored in plaintext.

Mitigation: Keep credentials out of project files and shell history; use a keychain or secret manager where available.

Risk: Some OFW reads and status summaries can change visible state or become stale if cache freshness is not checked.

Mitigation: Warn users before fetching unread message bodies, check completeness and freshness signals, and verify current draft or message state before presenting it as current.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw)
- [npm package declared by artifact](https://www.npmjs.com/package/ofw-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell, JSON configuration, and tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes cautions for freshness, completeness, draft lifecycle, mark-as-read behavior, and irreversible write actions.]

## Skill Version(s):

2.16.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
