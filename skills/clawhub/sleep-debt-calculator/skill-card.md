## Description:

Track sleep against an optimal target, calculate accumulated sleep debt, and suggest recovery schedules with chronotype detection, quality-weighted tracking, ASCII charts, and caffeine or alcohol impact monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to run a local Python command-line sleep tracker that records sleep sessions, estimates accumulated sleep debt, summarizes patterns, and suggests recovery timing. It is wellness guidance and not a medical diagnostic tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sleep logs and free-text notes can include sensitive health, routine, caffeine, or alcohol details and are saved locally in ~/.sleep_debt.json.

Mitigation: Avoid entering details you do not want stored on disk, protect the local account and home directory, and delete ~/.sleep_debt.json to reset or remove stored tracker data.

Risk: Sleep debt calculations and recovery suggestions may be mistaken for medical advice.

Mitigation: Use the output as general wellness tracking only, and consult a healthcare professional for persistent exhaustion, suspected sleep disorders, or other medical concerns.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/sleep-debt-calculator)
- [Server-resolved GitHub Repository](https://github.com/voronindenis5/sleep-debt-calculator)
- [Sleep Science Basics](references/sleep-science-basics.md)
- [Recovery Strategies](references/recovery-strategies.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and plain-text command-line output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled script stores user-entered sleep logs and notes locally in ~/.sleep_debt.json.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; SKILL.md frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
