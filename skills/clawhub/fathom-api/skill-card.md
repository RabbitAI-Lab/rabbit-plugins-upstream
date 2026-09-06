## Description:

Fathom API integration with managed OAuth for retrieving meeting recordings, transcripts, summaries, action items, and managing webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and operators use this skill to access Fathom meeting data through Maton, including meeting lists, recordings, transcripts, summaries, teams, team members, and webhook setup. It is intended for read-first workflows, with explicit confirmation before creating connections, webhooks, or deleting resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Fathom meeting data through a connected Maton account.

Mitigation: Install only when comfortable authorizing Maton for this data, prefer OAuth, choose the narrowest available Fathom scopes, and retrieve only the fields needed for the task.

Risk: Webhook creation, connection creation, and delete operations can change account state or expose meeting data to destination URLs.

Mitigation: Review webhook destination URLs and confirm the exact connection, resource, payload, and intended effect before any write or delete operation runs.

Risk: Using a Maton API key instead of OAuth increases the chance of credential exposure.

Mitigation: Prefer OAuth; if an API key is unavoidable, keep it out of command lines, logs, files, and user-visible output, and rotate it if exposed.

## Reference(s):

- [Fathom Skill Page](https://clawhub.ai/byungkyu/skills/fathom-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Fathom API Documentation](https://developers.fathom.ai)
- [Fathom LLM Reference](https://developers.fathom.ai/llms.txt)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, API paths, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide API calls that return JSON and meeting content from the connected Fathom account.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
