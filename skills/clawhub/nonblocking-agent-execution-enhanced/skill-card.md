## Description:

Nonblocking Agent Execution provides a jobctl.sh runner and operating guidance for launching long-running commands as detached jobs with bounded polling, durable local state, logs, verification, and optional callbacks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to keep long-running shell work from blocking agent turns, while preserving resumable job state, logs, status checks, cleanup, and callback-based notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands and job identifiers can affect local execution with the caller's privileges.

Mitigation: Use only as a trusted local administrative tool, validate commands and job IDs before execution, and run under a dedicated low-privilege account.

Risk: Callbacks, logs, output files, and persisted state can expose sensitive command output.

Mitigation: Protect the base directory, avoid callback payloads that contain sensitive data, and use only reviewed HTTPS callback endpoints.

Risk: Network-exposed wrappers around the runner can turn local job control into remote command control.

Mitigation: Do not expose the REST wrapper on a network unless it has been separately reviewed, authenticated, and constrained.

Risk: Unreviewed updates can change command, persistence, or callback behavior.

Mitigation: Pin installation to a reviewed release version or commit before operational use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/nonblocking-agent-execution-enhanced)
- [Skill Definition](artifact/SKILL.md)
- [README](artifact/README.md)
- [API Documentation](artifact/docs/API.md)
- [Integration Guide](artifact/docs/INTEGRATION.md)
- [Best Practices Guide](artifact/docs/BEST_PRACTICES.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands, JSON status examples, integration snippets, and local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local job state, logs, output files, optional webhook payloads, and command-line status responses.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and documentation state 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
