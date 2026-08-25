## Description:

Evaluate whether an article, document, video transcript, or webpage is worth reading; recommend full reading or specific sections; maintain a private local reading profile; and learn from explicit feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[langingsing](https://clawhub.ai/user/langingsing)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to decide whether shared articles, documents, transcripts, or webpages deserve full reading, targeted section reading, a summary-only pass, or a skip. It supports feedback-driven reading recommendations while maintaining a private local reading profile.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local reading profile can accumulate sensitive information about a user's interests and private reading material.

Mitigation: Set READWORTHY_STATE_DIR to a controlled local directory and install the skill only when persistent reading-profile storage is desired.

Risk: State edits can become inconsistent if article metadata, assessments, feedback events, or indexes are changed without the required maintenance steps.

Mitigation: Before each state write, run the backup script, append rather than rewrite historical events, rebuild the index after article changes, and validate the state.

Risk: Recommendations can be misleading when the agent only has a summary, excerpt, transcript fragment, or login-limited view of the source.

Mitigation: State the coverage limit, separate source facts from agent hypotheses, and avoid presenting an agent extension as the author's answer.

## Reference(s):

- [Readworthy state schema v2](references/state-schema-v2.md)
- [ClawHub skill page](https://clawhub.ai/langingsing/skills/readworthy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown recommendations with supporting evidence, reading scope, tradeoffs, and occasional shell commands for state setup or validation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update local JSON and JSONL state files when the user asks the agent to learn from assessments or feedback.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
