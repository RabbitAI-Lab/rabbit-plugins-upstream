## Description:

Operate Imgix through an OOMOL-connected account for reading sources, listing sources, updating sources, and purging asset cache entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Imgix through the OOMOL connector, including source lookup, source updates, and cache purge requests. It is intended for agents that need to inspect live action schemas before running Imgix actions with validated JSON payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends pipe-to-shell installer commands for the oo CLI.

Mitigation: Install the oo CLI from a verified package or a pinned installer with checksum or signature verification, and avoid elevated shells for remote installer commands.

Risk: The update_source and purge_asset actions can change Imgix state.

Mitigation: Confirm the exact payload, target, and expected effect before running write or destructive actions.

## Reference(s):

- [ClawHub Imgix skill](https://clawhub.ai/oomol/skills/oo-imgix)
- [Imgix homepage](https://www.imgix.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON action payloads and confirmation prompts for write or destructive Imgix actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
