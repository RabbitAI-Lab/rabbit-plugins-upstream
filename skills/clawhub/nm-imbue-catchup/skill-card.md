## Description:

Summarizes recent git changes for context recovery after session breaks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and project contributors use catchup to quickly understand what changed across repositories, documents, meeting notes, sprints, or logs after a gap and identify follow-up actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic status or summary requests may invoke the skill outside the intended context.

Mitigation: Specify the repository, document set, sprint, or log window that should be included in the catch-up analysis.

Risk: Catch-up summaries may include sensitive repository, log, or document content selected by the user.

Mitigation: Keep private or sensitive sources out of scope unless they are intended to be summarized.

Risk: Summaries and follow-up recommendations can omit context or overstate implications.

Mitigation: Review the relevant source files, logs, or notes before acting on important conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-catchup)
- [Claude Night Market imbue plugin](https://github.com/athola/claude-night-market/tree/master/plugins/imbue)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown summaries with bullets, checklists, and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Progressively loads git, document, or log analysis patterns based on the user's context.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
