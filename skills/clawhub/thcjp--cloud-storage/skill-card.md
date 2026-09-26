## Description:

Manages files across cloud providers with authentication, cost awareness, and multi-provider storage workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to manage cloud storage files and buckets across providers, including upload, download, listing, cost review, and cross-cloud migration tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests command execution and file access for cloud-storage work.

Mitigation: Install only in an agent environment where command execution is reviewed and scoped to the intended cloud-storage task.

Risk: Cloud operations can access production buckets, credentials, and billable resources.

Mitigation: Use least-privilege cloud credentials, test against non-production buckets first, and confirm provider billing and region settings before running changes.

Risk: The documentation mixes cloud-storage behavior with unrelated document, database, and code-review template text.

Mitigation: Treat the documented behavior as poorly scoped and review proposed commands, parameters, and outputs before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cloud-storage)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud file URLs, storage metadata, usage and cost reports, migration progress, and integrity-check results.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
