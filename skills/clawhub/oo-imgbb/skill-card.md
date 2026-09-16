## Description:

ImgBB lets an agent upload images through an OOMOL-connected ImgBB account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect the ImgBB connector schema, run an image upload action, and receive hosted image metadata without handling raw ImgBB API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute arbitrary code if followed.

Mitigation: Review setup commands before installing; prefer a trusted, versioned source with checksum or signature verification.

Risk: The upload action changes ImgBB account state by hosting an image.

Mitigation: Confirm the exact image and upload payload with the user before running ImgBB write actions.

## Reference(s):

- [ImgBB homepage](https://imgbb.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-imgbb)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with inline bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON data containing hosted image metadata and an execution identifier.]

## Skill Version(s):

1.0.3 (source: server evidence release version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
