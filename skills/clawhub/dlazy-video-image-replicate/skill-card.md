## Description:

This skill helps an agent study a user-provided reference image or video and recreate a similar look and structure with the user's own subject, product, or characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to invoke dLazy's video-image-replicate template for reference-based image or video remakes using their own prompts and media files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy's hosted service.

Mitigation: Do not attach confidential files unless upload is intended and approved for the use case.

Risk: Attached local files are uploaded to dLazy media storage before use.

Mitigation: Review file paths before using --files and attach only the intended reference or subject assets.

Risk: Project sessions can persist context across follow-up turns.

Mitigation: Check the project id before continuing prior work and use --clear when a fresh session is required.

Risk: A saved dLazy API key grants continued access until removed.

Mitigation: Rotate or revoke the API key when access should be removed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown/plain text with inline shell commands and streamed CLI responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference uploaded media or project sessions managed by the dLazy CLI.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
