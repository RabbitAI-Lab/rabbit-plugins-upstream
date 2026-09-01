## Description:

Stoic Coach guides users through Stoic reflection exercises, local journaling, progress review, dilemma mapping, recommendations, and daily quotes when they explicitly ask for Stoic practice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill as a Stoic practice coach for guided reflection, mood-aware exercise recommendations, local practice records, progress review, dilemma mapping, and daily Stoic quotes. It is intended for explicit Stoic-practice requests and is not a substitute for professional mental health care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Practice records may include sensitive personal reflections stored in plaintext local journaling.

Mitigation: Avoid entering secrets or highly sensitive details unless the data directory is protected; use an encrypted or access-controlled storage location when needed.

Risk: Synced data directories or exports may copy sensitive journal content outside the local machine.

Mitigation: Review export contents and destinations before creating backups, and use only trusted synced storage with appropriate access controls.

Risk: Mortality, loss, or other heavy reflection exercises may feel destabilizing for some users.

Mitigation: Pause deeper exercises when they feel overwhelming and seek professional mental health support for crisis signals or sustained impairment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bonniegeng-max/skills/stoic-coach)
- [Coach Guide](references/coach-guide.md)
- [Example Session](references/example-session.md)
- [Stoic Exercises](references/exercises.md)
- [Stoic Quotes](references/quotes.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and local JSON or Markdown export guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May append user-confirmed practice records to a local plaintext JSONL journal and export local records as Markdown or JSON.]

## Skill Version(s):

1.3.1 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
