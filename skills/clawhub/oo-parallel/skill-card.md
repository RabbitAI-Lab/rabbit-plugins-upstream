## Description:

Parallel (parallel.ai) lets agents read, create, and update data through the OOMOL-connected oo CLI instead of calling the Parallel API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Parallel through an OOMOL-connected account for web search, public URL extraction, structured data enrichment, and task-run creation or retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path tells agents to run a remote installer script directly in a shell.

Mitigation: Use a verified package or inspect the installer before execution, and do not let an agent automatically run the installer pipeline.

Risk: Creating a Parallel task run changes third-party service state.

Mitigation: Require user confirmation of the exact payload and expected effect before running write actions.

Risk: The skill depends on OOMOL's server-side credential flow for Parallel.

Mitigation: Install only when the publisher is trusted and the user is comfortable with server-managed credentials.

## Reference(s):

- [Parallel homepage](https://parallel.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-parallel)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector responses as JSON when the CLI is run with --json.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
