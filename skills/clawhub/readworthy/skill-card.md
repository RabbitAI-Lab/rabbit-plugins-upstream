## Description:

Evaluate whether an article, document, video transcript, or webpage is worth reading; recommend full reading or specific sections; maintain a private local reading profile; and learn from explicit feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[langingsing](https://clawhub.ai/user/langingsing)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use Readworthy to decide whether shared articles, documents, transcripts, or webpages merit full reading, section-level reading, summary-only treatment, or skipping. The skill maintains a local reading profile so future recommendations can account for prior knowledge and explicit feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores assessed content, feedback, profile details, and derived insights in local state.

Mitigation: Use READWORTHY_STATE_DIR to place state in a controlled location and manage or remove local state when working with sensitive sources.

Risk: Broad implicit activation for article and link tasks may apply the reading-profile workflow when a user expected a simpler response.

Mitigation: Confirm the desired scope when activation is ambiguous and distinguish source facts, profile-based synthesis, and agent hypotheses in the response.

Risk: Local reading history can become stale or misleading if corrections are overwritten or accepted silently.

Mitigation: Append feedback and revision events, preserve explicit corrections, keep inferred interpretations separate, rebuild the index, and validate state after writes.

## Reference(s):

- [Readworthy state schema v2](references/state-schema-v2.md)
- [Readworthy ClawHub skill page](https://clawhub.ai/langingsing/skills/readworthy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown recommendations with optional shell commands and local JSON state updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations use A/B/C/D reading scope labels, source evidence, estimated reading time, tradeoffs, and explicit uncertainty.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
