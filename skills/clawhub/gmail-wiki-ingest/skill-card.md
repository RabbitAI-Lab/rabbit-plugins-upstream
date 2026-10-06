## Description:

Triage Gmail threads against a personal knowledge wiki and propose which messages to save, review, or discard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samuel-wei](https://clawhub.ai/user/samuel-wei)

### License/Terms of Use:

MIT-0

## Use Case:

HiJavis users use this skill to sort recent Gmail conversations for their personal wiki, review suggested additions, and receive a digest of each run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads private Gmail metadata and may read up to 12 full threads per run.

Mitigation: Enable it only with the user's consent; Gmail discovery can be switched off in HiJavis, and full-text reads are limited to threads in the current batch.

Risk: Mail from trusted senders may be added to the wiki automatically.

Mitigation: Review the resulting cards and use the available undo action when an automatic addition is unwanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/samuel-wei/skills/gmail-wiki-ingest)
- [HiJavis iPhone app](https://apps.apple.com/us/app/hijavis/id6745134765)
- [Judgment rubric](rubric.md)
- [Banding and trust](references/banding-and-trust.md)
- [Tool contract](references/tool-contract.md)
- [Trigger contract](references/trigger-contract.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Structured verdicts]

**Output Format:** [JSON verdicts and a Markdown chat digest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [At most 12 staged email threads can be read in full per run.]

## Skill Version(s):

0.5.2 (source: ClawHub release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
