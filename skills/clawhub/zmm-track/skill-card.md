## Description:

Tracks commitments, expiry dates, watch items, in-flight diagnoses, and queues so an agent can surface due items at the right time without re-opening the original decision criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to record future commitments, expirations, watch signals, ongoing work, and queues, then check what is due. It is intended for local reminder and tracking workflows where due-time review should focus on previously written, verifiable conditions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist reminder and tracking records that may remain on disk over time.

Mitigation: Avoid recording sensitive business details; use aliases or redacted subjects for long-lived tracking files.

Risk: The skill may read prior zmm-track and common memory before responding.

Mitigation: Install only where persistent local tracking is desired and the memory locations are appropriate for the user.

Risk: Broad natural-language triggers could activate the tracking workflow unexpectedly.

Mitigation: Prefer explicit slash-command triggers when accidental activation would be disruptive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-track)
- [Publisher profile](https://clawhub.ai/user/iamzifei)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown and concise plain text with structured tracking-file guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local reminder and memory records when the host agent grants filesystem access.]

## Skill Version(s):

0.2.4 (source: server release metadata; artifact frontmatter lists 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
