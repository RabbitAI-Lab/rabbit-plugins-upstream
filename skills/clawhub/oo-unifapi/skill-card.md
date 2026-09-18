## Description:

UnifAPI lets agents read, create, and update data through the OOMOL `oo` CLI instead of calling the UnifAPI API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to inspect UnifAPI action schemas, run connector actions with JSON payloads, and retrieve execution metadata across supported social, SEO, content, maps, local search, events, and hotel services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote installer commands that could execute unreviewed code if run automatically.

Mitigation: Do not allow an agent to run installer commands automatically; install the oo CLI through a trusted, reviewable method and verify installer source and integrity before use.

Risk: Connector actions run through the user's connected OOMOL account and may consume account credits.

Mitigation: Confirm the account context and expected cost impact before running actions, and stop when OOMOL reports insufficient credit.

Risk: Write-tagged UnifAPI actions can change remote data.

Mitigation: Inspect the live action schema, confirm the exact payload and expected effect with the user, and avoid destructive or state-changing actions without explicit approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-unifapi)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [UnifAPI homepage](https://unifapi.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, JSON data, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [UnifAPI action responses include data and execution metadata from the connected OOMOL account.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
