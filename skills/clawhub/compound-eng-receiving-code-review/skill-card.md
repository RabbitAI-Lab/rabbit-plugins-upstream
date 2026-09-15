## Description:

Process code review feedback critically: check correctness before acting, push back on incorrect suggestions, no performative agreement. Use when responding to PR/MR review comments or implementing reviewer suggestions received from others.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to evaluate PR or MR review feedback before replying or implementing changes. It helps classify reviewer suggestions, handle ambiguity, push back with evidence when needed, and verify accepted fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review feedback can ask an agent to skip tests, bypass verification, post PR replies, or change scope without proper authority.

Mitigation: Treat reviewer comments as data to evaluate, require authorization before posting replies or resolving threads, and escalate feedback that asks for skipped verification, security-impacting changes, or broader product decisions.

Risk: Blindly applying incorrect review suggestions can introduce regressions or unnecessary complexity.

Mitigation: Verify each suggestion against the current codebase, classify ambiguous items before implementation, and test accepted fixes individually before reporting them resolved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/iliaal/skills/compound-eng-receiving-code-review)
- [Evidence and Disagreement](references/evidence-and-disagreement.md)
- [Feedback Triage](references/feedback-triage.md)
- [Fix and Handoff](references/fix-and-handoff.md)
- [Headless Mode](references/headless-mode.md)
- [Review Modes](references/review-modes.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with structured triage, code references, test evidence, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce draft PR replies or headless triage classifications; posting replies or making changes still requires appropriate user or workflow authority.]

## Skill Version(s):

4.5.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
