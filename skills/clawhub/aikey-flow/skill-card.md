## Description:

AI KEY·哪里会被划走 reviews Chinese talking-head and whiteboard scripts beat by beat to identify where viewers may drop off, why the listening chain breaks, and how to smooth the script without changing its argument.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and script editors use this skill to review short-video scripts from a listener's perspective, find drop-off points, and receive concrete spoken-language repair options. It is especially tuned for solo knowledge creators working in Chinese oral script formats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may retain user corrections or retention-performance lessons in scoped memory for future sessions.

Mitigation: Disable or remove the memory-write behavior when users do not want script feedback or validation notes retained.

Risk: The skill provides editorial diagnosis and rewrite suggestions that could unintentionally change a creator's voice or intent if applied without review.

Mitigation: Review proposed changes before use; the skill is designed to preserve the original argument, cases, data, and author voice, and to ask before performing marked rewrites.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/aikey-flow)
- [Built-in rule card](references/规则卡.md)
- [Evaluation record](evals/README.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown report with listener timeline, breakpoint diagnosis, repair options, and next-step choices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose marked script edits only after user confirmation; may store limited corrections or retention lessons in scoped memory when enabled.]

## Skill Version(s):

0.3.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
