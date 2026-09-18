## Description:

Buildkite (buildkite.com). Use this skill for Buildkite requests that read, create, and update data through the OOMOL-connected oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect Buildkite action schemas and operate Buildkite organizations, pipelines, builds, users, and access-token details through an OOMOL-connected account. It supports read workflows and confirmed write workflows such as creating, canceling, and rebuilding builds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documents remote pipe-to-shell installer commands for first-time setup.

Mitigation: Prefer a verified package or inspect and verify the installer before execution.

Risk: Buildkite token inspection and build creation, cancellation, or rebuild actions can expose sensitive account details or change CI state.

Mitigation: Run sensitive actions only after a clear user request, schema inspection, and explicit confirmation of the payload and expected effect.

## Reference(s):

- [ClawHub Buildkite Skill](https://clawhub.ai/oomol/skills/oo-buildkite)
- [Buildkite Homepage](https://buildkite.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
