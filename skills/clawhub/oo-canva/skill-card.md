## Description:

Canva (canva.com). Use this skill for Canva requests that read, create, or update Canva data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Canva through an OOMOL-connected account, including reading Canva user, design, asset, folder, and export metadata and initiating supported Canva write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions document remote installer commands that execute scripts from the internet without verification.

Mitigation: Prefer a verified, version-pinned installation path for the oo CLI and do not run remote installer commands blindly.

Risk: The skill can perform write actions that create designs, folders, export jobs, uploads, or move folder items in Canva.

Mitigation: Confirm the exact payload and expected effect with the user before running any state-changing Canva action.

Risk: The skill routes Canva actions through OOMOL-managed credentials.

Mitigation: Install and use it only when comfortable using OOMOL as an intermediary for Canva actions, and confirm the intended Canva account connection before use.

## Reference(s):

- [Canva homepage](https://www.canva.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-canva)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payloads; connector responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schemas before action payload construction]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
