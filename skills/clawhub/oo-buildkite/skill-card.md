## Description:

Buildkite (buildkite.com). Use this skill for Buildkite requests that read, create, or update Buildkite data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CI operators use this skill to inspect Buildkite organizations, pipelines, builds, users, and access-token details, and to create, cancel, or rebuild builds after confirming write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes CLI installation commands that pipe a remote script into a shell.

Mitigation: Use an official, version-pinned oo CLI installation method with checksum or signature verification before running Buildkite actions.

Risk: Buildkite create, cancel, and rebuild actions can change CI state.

Mitigation: Use a narrowly scoped Buildkite token and confirm the exact payload, target, and expected effect with the user before write actions.

Risk: Token-inspection actions can expose sensitive account or credential context if results are not redacted.

Mitigation: Invoke token-inspection only for diagnostics and verify returned token values are redacted before sharing output.

## Reference(s):

- [Buildkite homepage](https://buildkite.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Buildkite skill page](https://clawhub.ai/oomol/skills/oo-buildkite)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
