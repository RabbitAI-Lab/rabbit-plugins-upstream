## Description:

Creates a complete picture book from a theme by writing a paged story, generating consistent illustrations and matching background music, and assembling a portable HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators use this skill to turn a theme into a children's picture book, with paginated story text, consistent illustrations, and matching background music. The result is assembled as a portable HTML book.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to dLazy-hosted services, and generation may incur usage charges.

Mitigation: Avoid sending sensitive content, use only reference images you are authorized to upload, review account charges, and keep API keys private.

Risk: Downloaded media and generated book files are written to the local workspace.

Mitigation: Use a dedicated output folder and review generated files before sharing them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Image files, Audio files, HTML]

**Output Format:** [Paginated story data in JSON and a portable HTML picture book with image and music assets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to 10 pages; image and music assets use relative paths and can be opened offline when kept with the HTML book.]

## Skill Version(s):

1.3.32 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
