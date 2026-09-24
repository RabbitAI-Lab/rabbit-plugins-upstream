## Description:

Learns communication preferences from explicit feedback. Adapts tone, format, and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

External users and developers use this skill to let an agent remember explicitly confirmed communication-style preferences and adapt future responses while keeping preference memory transparent and removable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local preference memory may retain sensitive personal details if a user asks the agent to store them.

Mitigation: Do not store sensitive personal information; use the documented show and forget controls to review or remove stored entries.

Risk: Persistent style preferences can become stale or conflict with newer instructions.

Mitigation: Learn only from explicit feedback, ask when a preference is ambiguous, and let the most recent explicit statement win.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/chat)
- [Preference dimensions](dimensions.md)
- [Confirmation criteria](criteria.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown or plain text responses, with local preference files used as persistent configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local files under ~/chat for confirmed, experimental, and rejected preferences.]

## Skill Version(s):

1.1.0 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
