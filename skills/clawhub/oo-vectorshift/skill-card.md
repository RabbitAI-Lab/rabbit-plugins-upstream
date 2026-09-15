## Description:

VectorShift uses the OOMOL oo CLI connector to inspect VectorShift pipeline schemas, list and fetch pipelines, and run single or batch pipeline executions through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate VectorShift pipelines through an OOMOL-connected account, including schema inspection, pipeline discovery, and JSON-safe pipeline execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can execute an unverified remote OOMOL CLI installer.

Mitigation: Review the installer path first, prefer a signed or pinned installation method, and install only in environments where OOMOL CLI behavior is trusted.

Risk: The skill can run VectorShift pipelines, including bulk executions that may call external systems or consume credits.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running pipeline execution actions, especially bulk runs.

Risk: Credential handling depends on OOMOL server-side account connections.

Mitigation: Use only the intended OOMOL account connection, avoid exposing raw tokens, and retry setup only after an authentication or connection error requires it.

## Reference(s):

- [VectorShift homepage](https://vectorshift.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub VectorShift skill page](https://clawhub.ai/oomol/skills/oo-vectorshift)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads and returns connector responses that may include data and an execution ID.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
