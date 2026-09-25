## Description:

Automates job-application workflows by helping an agent search, configure, and submit applications using user-provided profile and application parameters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to automate repetitive job-application workflows, including profile-based application setup, batch submission, retry handling, and execution-status review. It should be used only where the user has explicitly approved each application submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may submit job applications or interact with external job platforms using personal profile data.

Mitigation: Require explicit user approval for each application submission and prefer dry-run or confirmation-required modes before any external submission.

Risk: The skill references API-key and personal-profile handling.

Mitigation: Provide only the minimum required credentials and profile data, store secrets in environment variables, and avoid broad or long-lived API keys.

Risk: The skill uses command execution and its sandboxing guarantees are unclear.

Mitigation: Run it only in an independently sandboxed agent environment and review generated shell commands before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/job-auto-apply)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON-shaped execution status examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run guidance, confirmation prompts, retry status, execution logs, and application-result summaries.]

## Skill Version(s):

1.0.1 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
