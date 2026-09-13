## Description:

Fathom API integration with managed OAuth for accessing meeting recordings, transcripts, summaries, action items, and approved webhook notifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to connect a Fathom account through Maton, retrieve or search meetings and recordings, and configure explicitly approved meeting-data automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting recordings, transcripts, summaries, and webhook payloads can contain highly sensitive participant and business data.

Mitigation: Use OAuth with the narrowest available scope, default to read-only operations, and avoid logging or storing raw meeting responses unless the user explicitly needs that output.

Risk: Webhook and destination_url flows can send meeting content to an external host or create ongoing delivery of future recordings.

Mitigation: Require explicit approval for the exact destination host, payload flags, and ongoing scope before enabling callbacks or webhooks; keep transcript forwarding off unless it is necessary.

Risk: API-key fallback can expose a long-lived credential if copied into shell history, logs, or child process environments.

Mitigation: Prefer OAuth; when an API key is unavoidable, keep it in the credential store or a narrowly scoped runtime environment and rotate it if exposed.

## Reference(s):

- [Fathom API Documentation](https://developers.fathom.ai)
- [Fathom LLM Reference](https://developers.fathom.ai/llms.txt)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/fathom-api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with inline shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands operate through Maton OAuth or API-key credentials and may return sensitive Fathom meeting data.]

## Skill Version(s):

1.2.5 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
