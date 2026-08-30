## Description:

Show ken measured impact as a scoreboard from its own benchmark results. Honest empty state when none exist. One-shot display.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rajnandan1](https://clawhub.ai/user/rajnandan1)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to display measured Ken benchmark medians as a concise scoreboard, or an honest empty state when no benchmark results exist.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill could mislead users if it presents unmeasured or live per-repository savings as benchmark results.

Mitigation: Show only existing Ken benchmark medians or the documented empty state, and point users to the counted ledger instead of inventing a savings number.

Risk: Users may expect the skill to modify files or change agent mode.

Mitigation: Keep the behavior to a one-shot display and avoid edits, persistence, or mode changes.

## Reference(s):

- [Ken project homepage](https://github.com/rajnandan1/ken)
- [ClawHub skill page](https://clawhub.ai/rajnandan1/skills/ken-gain)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text or Markdown-compatible scoreboard with ASCII bars]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One-shot display; should not edit files, persist state, or claim live per-repository savings.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
