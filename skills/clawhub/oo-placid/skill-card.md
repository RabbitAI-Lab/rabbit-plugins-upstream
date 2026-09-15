## Description:

Placid (placid.app) helps agents read, create, retrieve, list, and delete Placid image requests and templates through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Placid templates and image generation requests through the OOMOL oo CLI, including inspecting live action schemas before creating payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands for the oo CLI.

Mitigation: Review setup commands before installation and prefer an official pinned package or verified installer.

Risk: Write and destructive Placid actions can change or delete data.

Mitigation: Confirm the exact target, payload, and expected effect before running write or delete actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-placid)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Placid homepage](https://placid.app)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should inspect the live connector schema before payload construction and return JSON responses from the oo CLI.]

## Skill Version(s):

1.0.3 (source: artifact metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
