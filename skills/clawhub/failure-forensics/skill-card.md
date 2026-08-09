## Description:

Use when an agent task fails or produces unexpected results. Performs structured post-mortem root cause analysis: categorizes the failure, traces the exact failure point through tool-call logs, reconstructs the decision chain, generates a post-mortem report, and saves lessons to prevent recurrence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill after a failed or unexpected agent task to categorize the failure, reconstruct the timeline, trace root causes, and produce a durable post-mortem report with lessons learned.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Failure logs and saved post-mortem reports can contain tokens, credentials, personal data, internal paths, prompts, or sensitive command output.

Mitigation: Review and redact sensitive content before saving or sharing reports, and store generated artifacts only in locations with appropriate access controls.

## Reference(s):

- [Failure Taxonomy](references/failure-taxonomy.md)
- [Post-Mortem Report Template](references/post-mortem-template.md)
- [Source Repository](https://github.com/voronindenis5/failure-forensics)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/failure-forensics)
- [Publisher Profile](https://clawhub.ai/user/voronindenis5)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Files]

**Output Format:** [Markdown reports, timeline summaries, classifications, and command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled Python script accepts JSON or JSONL tool-call logs and can write timeline or post-mortem Markdown files.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
