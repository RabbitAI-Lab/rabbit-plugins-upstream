## Description:

VectorShift (vectorshift.ai). Use this skill for ANY VectorShift request - searching and reading data. Whenever a task involves VectorShift, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect VectorShift pipeline schemas, list or fetch accessible pipelines, and run single or batch pipeline executions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: VectorShift pipeline runs can have effects that are not obvious from the action name.

Mitigation: Inspect the live schema and pipeline details before building payloads, and confirm the exact effect with the user before running actions that may change state.

Risk: Requests and pipeline inputs are routed through an OOMOL-connected account.

Mitigation: Use the skill only with data approved for the connected VectorShift and OOMOL account, and verify account scopes before sensitive runs.

Risk: The first-time setup guidance includes remote installer commands for the oo CLI.

Mitigation: Prefer a verified or package-manager-based oo CLI installation path, or review installer scripts before execution.

## Reference(s):

- [VectorShift homepage](https://vectorshift.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [VectorShift skill listing](https://clawhub.ai/oomol/skills/oo-vectorshift)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live VectorShift connector schemas before execution; command responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
