## Description:

This skill helps an agent track future commitments, expiry dates, watch-items, in-flight diagnoses, and publication queues, then surface due items without re-litigating the original trigger condition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to keep dated commitments, expirations, monitoring checks, work-in-progress state, and publication queues available across sessions so due follow-ups are surfaced at the right time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases may activate the tracking workflow unintentionally.

Mitigation: When intent is ambiguous, confirm whether the user wants to record, review, or continue tracking items before writing or updating records.

Risk: Long-lived tracking files and memory notes may retain sensitive names, amounts, or confidential details.

Mitigation: Use aliases or redaction for sensitive entities and avoid recording unnecessary confidential details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-track)
- [Publisher profile](https://clawhub.ai/user/iamzifei)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Concise text responses and Markdown tracking records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create long-lived scoped tracking files and memory notes when configured.]

## Skill Version(s):

0.2.1 (source: server release evidence; artifact frontmatter reports 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
