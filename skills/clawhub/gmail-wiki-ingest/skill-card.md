## Description:

Triage a batch of the user's email against their personal knowledge wiki and hand the verdicts back to javis-server, which bands them into auto-ingest / review card / auto-discard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samuel-wei](https://clawhub.ai/user/samuel-wei)

### License/Terms of Use:

MIT-0

## Use Case:

External HiJavis users use this skill to review Gmail thread metadata against their personal wiki, identify durable correspondence, and queue or apply wiki ingest decisions through the HiJavis review flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads Gmail thread metadata on a scheduled basis.

Mitigation: Enable it only when the HiJavis Gmail ingest switch and read-only Gmail grant match the user's expectations.

Risk: The security summary flags contradictory execution notes in the bundle.

Mitigation: Ask the publisher to resolve the execution-note contradiction before relying on broad deployment.

Risk: Email subjects and sender metadata can contain misleading instructions or weak signals.

Mitigation: Treat email content as data, judge only from metadata, cite only returned wiki slugs, and rely on server validation plus review cards for final outcomes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/samuel-wei/skills/gmail-wiki-ingest)
- [Tool Contract](references/tool-contract.md)
- [Banding and Trust](references/banding-and-trust.md)
- [Trigger Contract](references/trigger-contract.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Structured JSON verdicts submitted through the bundled CLI, with a short text summary only for manual runs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes one metadata-only Gmail candidate batch per run; empty scheduled batches are silent.]

## Skill Version(s):

0.3.0 (source: package.json, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
