## Description:

Gmail Wiki Ingest reviews Gmail thread metadata against a user's personal wiki, returns one verdict per candidate, and reports each run while server-side controls handle message access, banding, trust, validation, and writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samuel-wei](https://clawhub.ai/user/samuel-wei)

### License/Terms of Use:

MIT-0

## Use Case:

HiJavis users use this skill to triage recent Gmail threads for a personal wiki, surfacing correspondence for confirmation while filtering receipts, newsletters, and service notices. It supports daily and on-demand email-to-wiki ingestion after Gmail is connected in the HiJavis iPhone app.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes Gmail metadata during daily or on-demand runs, which may expose sensitive sender and subject context to the agent.

Mitigation: Enable the skill only after reviewing the HiJavis Gmail ingest switch and read-only Gmail connection; keep it disabled when this metadata triage is not desired.

Risk: A trusted sender can qualify for automatic ingest after repeated confirmations.

Mitigation: Review trusted-sender behavior before enabling the skill, and use Confirm, Discard, or available undo flows to keep sender trust aligned with the user's intent.

Risk: Email subjects or sender fields can contain misleading instructions aimed at the agent.

Mitigation: Treat fetched mail fields as data to classify, not instructions, and rely on server-side controls for banding, reference validation, and writes.

## Reference(s):

- [README](README.md)
- [Tool Contract](references/tool-contract.md)
- [Banding and Trust](references/banding-and-trust.md)
- [Trigger Contract](references/trigger-contract.md)
- [HiJavis iPhone App](https://apps.apple.com/us/app/hijavis/id6745134765)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON verdict/report payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetch returns Gmail metadata only; each run ends with a chat digest, including empty batches.]

## Skill Version(s):

0.4.0 (source: server release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
