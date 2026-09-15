## Description:

Shortcut lets an agent read, create, and update Shortcut data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and teams with an OOMOL-connected Shortcut workspace use this skill to let an agent inspect schemas, retrieve Shortcut records, search stories, and prepare confirmed create or update actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute code on the user's machine.

Mitigation: Prefer official package-manager or manually verified installation steps, and avoid running pipe-to-shell installers blindly.

Risk: Create and update actions can change Shortcut workspace data.

Mitigation: Confirm the exact action payload and expected effect with the user before running any write operation.

Risk: Shortcut operations are routed through OOMOL's connector with server-side credential handling.

Mitigation: Install only if the user trusts OOMOL and is comfortable using an OOMOL-connected Shortcut account.

## Reference(s):

- [Shortcut skill on ClawHub](https://clawhub.ai/oomol/skills/oo-shortcut)
- [Shortcut homepage](https://www.shortcut.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Shortcut connector responses returned as JSON when actions are run.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
