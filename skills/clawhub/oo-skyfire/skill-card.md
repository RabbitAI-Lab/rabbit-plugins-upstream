## Description:

Skyfire (skyfire.xyz). Use this skill for ANY Skyfire request — reading, creating, and updating data. Whenever a task involves Skyfire, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Skyfire through an OOMOL-connected account, including marketplace service lookup and buyer-token creation. The skill guides the agent to inspect live action schemas before sending JSON payloads through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to run remote installer scripts directly in a shell.

Mitigation: Install the oo CLI from a verified, version-pinned source, or inspect and verify the installer before running it.

Risk: The create_token action can create funded or identity-carrying buyer tokens.

Mitigation: Confirm the exact create_token payload and intended effect with the user before execution.

Risk: Connector inputs can drift from examples or assumptions.

Mitigation: Fetch the live action schema with `oo connector schema` before constructing or running any payload.

## Reference(s):

- [ClawHub Skyfire Skill](https://clawhub.ai/oomol/skills/oo-skyfire)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Skyfire Homepage](https://skyfire.xyz)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Skyfire connector schemas before action execution; oo CLI responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
