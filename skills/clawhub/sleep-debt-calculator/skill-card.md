## Description:

Track sleep vs optimal, calculate accumulated sleep debt, and suggest evidence-based recovery schedules with chronotype detection, quality-weighted tracking, ASCII charts, and caffeine/alcohol impact monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to track nightly sleep, calculate accumulated sleep debt against age-based targets, and plan recovery schedules from local command-line data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sleep logs and free-text notes are stored as a local plaintext wellness journal.

Mitigation: Avoid entering highly sensitive details on shared or backed-up devices, and delete ~/.sleep_debt.json to reset or remove stored data.

Risk: Sleep debt estimates and recovery suggestions are wellness guidance, not medical diagnosis or treatment.

Mitigation: Treat outputs as informational and consult a qualified healthcare provider for persistent insomnia, daytime sleepiness, suspected sleep apnea, or other health concerns.

## Reference(s):

- [Sleep Science Basics](artifact/references/sleep-science-basics.md)
- [Recovery Strategies](artifact/references/recovery-strategies.md)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/sleep-debt-calculator)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with command-line examples and local JSON-backed sleep tracking outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores profile data, sleep logs, quality notes, and reports locally in ~/.sleep_debt.json.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
