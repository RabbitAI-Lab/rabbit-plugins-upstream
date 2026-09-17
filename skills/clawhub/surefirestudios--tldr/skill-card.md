## Description:

Leads agent responses with a concise TL;DR while preserving full detail and providing a parseable agent-to-agent report format.

This skill is ready for commercial/non-commercial use.

## Publisher:

[surefirestudios](https://clawhub.ai/user/surefirestudios)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to make long assistant responses easier to scan while preserving details that affect decisions. It is useful for human-facing answers, handoffs, commit messages, and PR bodies that need concise summaries without losing important context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can keep changing response style for the rest of a session until it is turned off.

Mitigation: Use it when TL;DR-first formatting is desired, and turn it off explicitly with stop tldr, tldr off, normal mode, or /tldr full.

Risk: Broad phrases such as more or normal mode may be interpreted as formatting controls.

Mitigation: Use explicit wording for follow-up requests and mode changes when response formatting matters.

Risk: Summaries can hide important consequences if critical material is folded into detail.

Mitigation: Keep destructive actions, security findings, data loss, money or quota impacts, verbatim errors, diffs, legal or medical boundaries, and requested full output visible above any fold.

## Reference(s):

- [tldr reference](artifact/reference.md)
- [Project homepage](https://github.com/SurefireStudios/tldr)
- [ClawHub skill page](https://clawhub.ai/surefirestudios/skills/tldr)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text with TL;DR lines, optional detail folds, and parseable tldr blocks for agent-to-agent reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default depth is three summary lines; never-compress items remain visible, and brief mode can hold non-critical detail until requested.]

## Skill Version(s):

0.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
