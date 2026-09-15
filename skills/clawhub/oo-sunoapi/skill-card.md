## Description:

SunoAPI (sunoapi.org) helps agents inspect live SunoAPI action schemas and run OOMOL-connected SunoAPI requests for reading, creating, and updating music-related data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate SunoAPI through an OOMOL-connected account for music generation, lyrics, sounds, MIDI, covers, audio editing tasks, task status retrieval, and credit checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote SunoAPI task creation can consume credits or process user-supplied media.

Mitigation: Require explicit user confirmation of the exact action, payload, uploaded content, and possible credit use before generation, upload, conversion, extension, separation, cover, or similar task-submission actions.

Risk: First-time setup includes shell installer commands from remote URLs.

Mitigation: Use the skill only when the OOMOL CLI installation source is trusted, and inspect installer scripts before executing them.

Risk: Live action schemas and account connections can change outside the skill artifact.

Mitigation: Inspect the live action schema before constructing payloads and verify the OOMOL/SunoAPI account connection before relying on returned task identifiers or account state.

## Reference(s):

- [SunoAPI homepage](https://sunoapi.org)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub SunoAPI skill page](https://clawhub.ai/oomol/skills/oo-sunoapi)
- [SunoAPI icon](https://static.oomol.com/logo/third-party/sunoapi.png)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SunoAPI task identifiers, execution identifiers, action schemas, account credit information, or command guidance.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
