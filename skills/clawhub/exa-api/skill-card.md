## Description:

Exa API integration with managed API key authentication for neural web search, page content retrieval, similar page discovery, AI-generated answers, and async research tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search the web, retrieve URL contents, find similar websites, generate cited answers, and run deep research tasks through an authenticated Exa connection managed by Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects Exa through Maton's gateway and depends on authenticated user connections.

Mitigation: Install only if the user trusts Maton, prefer OAuth, and use a dedicated Maton account with only the needed connections.

Risk: API keys or access tokens could be exposed through environment variables, command history, logs, or pasted output.

Mitigation: Prefer OAuth and operating-system credential storage; do not expose API keys, and rotate keys if they are printed, committed, or pasted.

Risk: Connection creation, writes, hosted functions, and trigger automation can act on the user's authorized Exa or Maton resources.

Mitigation: Confirm every connection, write, deployment, invocation, and automation step with the user before execution.

Risk: Scheduled or event-triggered automation can run without repeated interactive prompts once approved.

Mitigation: Choose the user's intended timezone for schedules and review the target function, connections, and network policy before deploying triggers.

## Reference(s):

- [ClawHub Exa skill listing](https://clawhub.ai/byungkyu/skills/exa-api)
- [Maton homepage](https://maton.ai)
- [Exa API Documentation](https://exa.ai/docs)
- [Exa API Reference](https://exa.ai/docs/reference/search)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, API calls]

**Output Format:** [Markdown with inline shell, Python, HTTP, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include authenticated Exa and Maton API responses; users should avoid exposing raw credentials or unnecessary personal data.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
