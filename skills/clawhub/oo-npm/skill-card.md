## Description:

npm (npmjs.com). Use this skill for ANY npm request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query npm package, version, download, user, and advisory information through the OOMOL oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags unverified remote installer commands in fallback setup guidance.

Mitigation: Prefer a verified, signed, or package-manager installation method and review installer contents before execution.

Risk: npm requests are routed through an account-linked third-party connector.

Mitigation: Install only when comfortable using OOMOL as an intermediary and review what npm data will be sent through the connector.

## Reference(s):

- [ClawHub npm skill page](https://clawhub.ai/oomol/skills/oo-npm)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [npm homepage](https://www.npmjs.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
