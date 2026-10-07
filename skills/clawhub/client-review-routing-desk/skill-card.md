## Description:

Selects a recipient for a client brief and records a finance-review message in a local mail queue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Client communications staff and agents use the skill to choose a contact for a client brief and prepare a finance-review queue entry for that recipient. The local queue entry does not confirm that an email was sent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the downstream operation writes a local mail-queue JSON artifact.

Mitigation: Use a dedicated, writable output directory and review the artifact before further use.

Risk: A generated queue entry could be mistaken for an email that was sent.

Mitigation: Treat the queue entry as a local draft or record, not proof of delivery.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/client-review-routing-desk)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON recipient or queue-entry result, with a local JSON mail-queue artifact for downstream runs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The downstream operation requires a writable output directory; a queue entry is not evidence of delivery.]

## Skill Version(s):

3.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
