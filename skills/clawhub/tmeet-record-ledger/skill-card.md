## Description:

Use the complete official Tencent Meeting record command family to locate recordings, retrieve native smart-minutes summaries and Todos, verify evidence in transcripts, handle recording-access requests, and produce a source-labeled meeting Todo ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[metaphor279](https://clawhub.ai/user/metaphor279)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and meeting operators use this skill to find Tencent Meeting recordings, retrieve native smart-minutes summaries and Todos, verify transcript evidence, and prepare source-labeled meeting summaries and Todo ledgers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an authenticated Tencent Meeting CLI to search recordings and read smart minutes or transcripts.

Mitigation: Install it only when that meeting-recording access is intended for the agent and the authenticated account is appropriate.

Risk: Playback or download links may contain temporary credentials.

Mitigation: Treat links as sensitive, show them only on explicit request, and avoid placing them in the Todo ledger.

Risk: Recording-access requests require user review before an approval request is submitted.

Mitigation: Review the request details and confirm in a later message before allowing the agent to submit the access request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/metaphor279/skills/tmeet-record-ledger)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown meeting summary and Todo ledger with source labels, plus CLI commands or guidance when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source labels, transcript references, meeting metadata, and explicit confirmation steps for access requests.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
