## Description:

Helps developers, support teams, SaaS operators, and users turn vague errors into clear messages that explain what failed, why it failed, and what action to take next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, SaaS operators, and users use this skill to improve error messages, troubleshooting workflows, checklists, implementation notes, and decision support for clearer user feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording may invoke the skill for generic debugging or support prompts beyond error-message improvement.

Mitigation: Use the skill when the task is about improving user-facing error messages or troubleshooting workflows, and tighten trigger wording before deployment if predictable activation is required.

Risk: Generated guidance can be misleading when the underlying failure mode, logs, or product behavior are incomplete.

Mitigation: Review proposed wording and workflows against actual failure evidence, support policy, and product behavior before shipping user-facing changes.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/error-message-improver)
- [SourceMeta JSON Schema issue 842](https://github.com/sourcemeta/jsonschema/issues/842)
- [ani-cli issue 1893](https://github.com/pystardust/ani-cli/issues/1893)
- [Operator issue 16835](https://github.com/yrn-dev/Operator/issues/16835)
- [Dacelo type-inference RFC issue](https://github.com/sizumita/dacelo/issues/1)
- [SegmentFault error-messages tag](https://segmentfault.com/t/error-messages)
- [Hacker News discussion on Zig pointer stability](https://news.ycombinator.com/item?id=49502293)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown response with optional code, command, checklist, or configuration blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions, validation notes, and follow-up risks when useful.]

## Skill Version(s):

0.20260907.40414 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
