## Description:

Show ken measured impact as a scoreboard from its own benchmark results. Honest empty state when none exist. One-shot display.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rajnandan1](https://clawhub.ai/user/rajnandan1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use ken-gain to display measured ken benchmark impact as a one-shot scoreboard. It reports only recorded benchmark medians and provides an honest empty state when no benchmark results exist.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Output could be mistaken for per-repository savings or estimated results.

Mitigation: Report only measured medians from ken benchmark results and avoid claims that were not measured.

Risk: Users may expect the display helper to generate benchmarks or modify local state.

Mitigation: Treat the skill as a one-shot display helper; benchmark generation is separate and may require user-managed API keys.

## Reference(s):

- [ken repository](https://github.com/rajnandan1/ken)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Plain text or Markdown scoreboard with ASCII bars]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One-shot display; does not write files, change modes, or persist state.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
