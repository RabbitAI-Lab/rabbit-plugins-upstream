## Description:

Fairing (fairing.co). Use this skill for ANY Fairing request - searching and reading data. Whenever a task involves Fairing, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Fairing through an OOMOL-connected account, inspect live action schemas, and list paginated Fairing survey responses with optional filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes direct execution of remote installer scripts.

Mitigation: Install only after trusting OOMOL's installer source; prefer a verified, version-pinned package or inspect and verify the installer first.

Risk: Incorrect Fairing request payloads can occur if the agent relies on stale action details.

Mitigation: Fetch the live action schema with the oo CLI before constructing a payload.

## Reference(s):

- [Fairing homepage](https://fairing.co)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs the agent to inspect the live Fairing action schema before constructing requests; connector responses are JSON.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
