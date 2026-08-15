## Description:

Use when an agent task fails or produces unexpected results. Performs structured post-mortem root cause analysis: categorizes the failure, traces the exact failure point through tool-call logs, reconstructs the decision chain, generates a post-mortem report, and saves lessons to prevent recurrence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill after failed or unexpected agent task outcomes to classify the failure, reconstruct the tool-call timeline, identify root cause, and produce a durable post-mortem report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Failure logs and generated post-mortems may retain sensitive details such as tokens, credentials, customer data, prompts, internal URLs, stack traces, or file paths.

Mitigation: Review and redact logs and reports before saving or sharing them, and require explicit approval before publishing them to issue trackers or knowledge bases.

Risk: Persisted post-mortems can accumulate sensitive session details if storage location and retention are not controlled.

Mitigation: Use a controlled local post-mortems directory or approved knowledge base with appropriate access controls and retention practices.

## Reference(s):

- [Source repository](https://github.com/voronindenis5/failure-forensics)
- [Failure taxonomy](references/failure-taxonomy.md)
- [Post-mortem report template](references/post-mortem-template.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown reports, text classifications, and shell command guidance for the bundled Python script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The analyzer accepts JSON or JSONL tool-call logs and can write timeline or post-mortem Markdown files.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
