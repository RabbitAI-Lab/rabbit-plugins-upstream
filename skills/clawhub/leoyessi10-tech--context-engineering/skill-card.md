## Description:

Guides agents through context compression, structured summarization, token usage reduction, and evaluation for long-running sessions that exceed context limits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leoyessi10-tech](https://clawhub.ai/user/leoyessi10-tech)

### License/Terms of Use:


## Use Case:

Developers and agent builders use this skill to design compression workflows, preserve task continuity, and evaluate whether compacted context retains the details needed for coding and debugging sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Compressed context can contain private code, file paths, secrets, or user data when real conversations are evaluated with a remote LLM judge.

Mitigation: Require consent, redact sensitive content, and review provider terms before adapting the documented judge workflow to production data.

Risk: Context compression can drop file paths, decisions, error messages, or other artifact-trail details needed for reliable continuation.

Mitigation: Use structured summaries with explicit artifact sections and probe-based checks before relying on compressed context for coding work.

## Reference(s):

- [Context Compression Evaluation Framework](artifact/references/evaluation-framework.md)
- [ClawHub Skill Page](https://clawhub.ai/leoyessi10-tech/skills/context-engineering)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured summary templates, evaluation rubrics, and implementation guidance for context compression workflows.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
