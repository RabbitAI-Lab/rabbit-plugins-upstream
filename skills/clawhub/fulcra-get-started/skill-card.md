## Description:

Guides a new user or agent through the initial setup, configuration, and capabilities of the Fulcra environment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fulcra](https://clawhub.ai/user/fulcra)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to connect a user to Fulcra, understand Fulcra's onboarding options, and move toward a useful first workflow with shared context, workspaces, ingestion, and visibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help an agent connect to Fulcra, a remote platform that may include sensitive personal data and remote storage.

Mitigation: Connect only data sources the user intends to share with Fulcra and avoid uploading secrets or regulated personal data unless explicitly intended.

Risk: The Fulcra CLI stores refreshable credentials locally after authentication.

Mitigation: Treat the local credential file as sensitive and review local environment access before authenticating.

## Reference(s):

- [Fulcra CLI](references/fulcra-cli.md)
- [Fulcra Website](https://www.fulcradynamics.com/)
- [Fulcra REST API Documentation](https://fulcradynamics.github.io/developer-docs/api-reference/)
- [Fulcra Python SDK and CLI Source](https://github.com/fulcradynamics/fulcra-api-python/)
- [Fulcra MCP Documentation](https://fulcradynamics.github.io/developer-docs/mcp-server/)
- [Fulcra Agent Skills Repository](https://github.com/fulcradynamics/agent-skills)
- [Fulcra Cookbook](https://www.fulcradynamics.com/resources/cookbook)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash code blocks and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide authentication, data-source connection, remote file use, and follow-on skill selection.]

## Skill Version(s):

0.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
