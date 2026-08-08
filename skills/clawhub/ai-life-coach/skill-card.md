## Description:

AI Life Coach guides users through Socratic dialogue for self-awareness, goal clarification, emotional support, and action planning, with crisis signals routed to a safety-first assessment before coaching.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luhayden-blip](https://clawhub.ai/user/luhayden-blip)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users use this skill for structured life-coaching conversations that clarify goals, examine personal patterns, and turn reflections into next actions. The skill also supports local coaching memory and optional reflection summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores sensitive emotional coaching memory and summaries on the local device.

Mitigation: Use it only on trusted personal devices or accounts, avoid entering identifying details, and review or delete local memory files when privacy risk changes.

Risk: The optional export and upload flow may disclose sensitive personal patterns to an external site.

Mitigation: Treat export or upload as external disclosure, inspect the exported JSON before sharing, and decline the optional sharing prompt when disclosure is not appropriate.

Risk: Users may mistake life-coaching and emotional-support output for professional mental health care.

Mitigation: Keep the coaching boundary clear, use the crisis-first assessment for self-harm signals, and direct users with sustained distress or crisis risk to qualified professionals or crisis resources.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Conversational text with optional Markdown reports, JSON memory summaries, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local coaching memory, reflection reports, and optional export JSON through bundled scripts.]

## Skill Version(s):

2.0.4 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
