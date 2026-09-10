## Description:

Process code review feedback critically: check correctness before acting, push back on incorrect suggestions, and avoid performative agreement when responding to PR/MR review comments or implementing reviewer suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to triage incoming code review feedback, verify technical premises against the current codebase, decide whether to fix, defer, clarify, or push back, and prepare evidence-based responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide an agent to inspect repository content and PR review comments, then draft or post review-thread replies.

Mitigation: Keep approval gates for public comments, resolving threads, and automated headless workflows.

Risk: Blindly accepting reviewer comments can introduce incorrect code changes or skip needed verification.

Mitigation: Triage and verify every finding against code, tests, documentation, history, or reproduction evidence before implementing or replying.

## Reference(s):

- [Evidence and disagreement](references/evidence-and-disagreement.md)
- [Feedback triage](references/feedback-triage.md)
- [Fix and handoff](references/fix-and-handoff.md)
- [Headless mode](references/headless-mode.md)
- [Review modes](references/review-modes.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance, triage summaries, proposed code changes, shell commands, and review-thread reply drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return structured headless triage groups such as AUTO-FIX, AUTO-DECLINE, ESCALATE, and PRIOR FEEDBACK when invoked programmatically.]

## Skill Version(s):

4.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
