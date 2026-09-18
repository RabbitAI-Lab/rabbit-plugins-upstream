## Description:

Stability AI (stability.ai). Use this skill for Stability AI requests through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run Stability AI connector actions through the oo CLI with OOMOL-managed credentials. The documented action generates audio from text prompts and uploads the result to connector transit storage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports that setup instructions include direct execution of unverified remote installer scripts in a shell.

Mitigation: Prefer official package-manager installation or manually inspected, version-pinned downloads with checksums or signatures before installing the oo CLI.

Risk: The security evidence notes that the skill trigger wording is broader than the documented Stability AI action.

Mitigation: Confirm the exact connector action and payload with the live schema before running an action.

Risk: Connector actions may consume account credits or create generated assets.

Mitigation: Inspect the action schema first and confirm payload, expected cost-sensitive behavior, and destination before execution.

## Reference(s):

- [ClawHub Stability AI skill page](https://clawhub.ai/oomol/skills/oo-stabilityai)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Stability AI homepage](https://stability.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are JSON when run with the documented --json flag.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
