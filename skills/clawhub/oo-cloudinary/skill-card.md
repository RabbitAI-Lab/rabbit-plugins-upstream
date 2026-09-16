## Description:

Cloudinary helps agents read, create, and update Cloudinary assets through an OOMOL-connected Cloudinary connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to list, inspect, upload, rename, and update Cloudinary assets from an agent session without handling raw Cloudinary credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Verify the OOMOL installer through trusted vendor documentation, checksums, signatures, or manual inspection before running curl-to-bash or irm-to-iex commands.

Risk: Upload, rename, and update actions can change Cloudinary asset state.

Mitigation: Inspect the live action schema and confirm the exact payload and intended effect before running write actions.

Risk: Cloudinary actions are routed through OOMOL as an intermediary.

Mitigation: Install only when use of OOMOL for Cloudinary actions is acceptable for the user's account and data handling requirements.

## Reference(s):

- [ClawHub Cloudinary skill page](https://clawhub.ai/oomol/skills/oo-cloudinary)
- [Cloudinary homepage](https://cloudinary.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON responses from oo connector actions when commands are executed.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
