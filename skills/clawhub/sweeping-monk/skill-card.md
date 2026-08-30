## Description:

Sweeping Monk is a research and academic advising skill that helps users diagnose methodology, research design, critical thinking, academic writing, and communication blockers while delegating literature search and citation verification to specialized skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, graduate students, academic writers, and research advisors use this skill to clarify research questions, choose methods, critique arguments, plan study designs, and break through stuck points in scholarly work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent local usage records may remain on the user's machine.

Mitigation: Decide before use whether local logging is acceptable; disable it using the skill's documented opt-out command if it is not needed.

Risk: Cloud telemetry may upload method-level usage signals.

Mitigation: Disable cloud upload before use when telemetry is not acceptable, and inspect the documented cloud configuration URLs before enabling it.

Risk: Cloud-driven proposal or update workflows could modify local skill files.

Mitigation: Run proposal approval or application flows only as the skill creator or maintainer, and review the full diff and target paths first.

Risk: Cross-skill signal processing may affect future guidance behavior.

Mitigation: Periodically inspect or clear local signal records if reproducibility or isolation of advising behavior matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j-levee/skills/sweeping-monk)
- [Introduction](references/intro.md)
- [Research playbook](references/research-playbook.md)
- [Method matrix](references/method-matrix.md)
- [Cognitive apprenticeship](references/cognitive-apprenticeship.md)
- [Double-loop learning](references/double-loop.md)
- [Signals specification](references/signals.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Text or Markdown guidance, with code, shell command, or configuration snippets when explicitly requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory-first output; tool use is reserved for explicit implementation, calculation, or external verification requests.]

## Skill Version(s):

1.11.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
