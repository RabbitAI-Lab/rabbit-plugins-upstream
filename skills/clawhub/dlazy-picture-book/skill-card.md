## Description:

Creates a complete picture book from a theme, with a paged story, style-consistent illustrations, matching background music, and a self-contained HTML reader.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask the agent to turn a theme into a children's picture book or bedtime story, then read or share it as an HTML book.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are uploaded to dLazy services; untrusted book.json image paths may be unsafe in generated HTML.

Mitigation: Use content intended for the hosted service, work in a dedicated output folder, and use trusted book.json paths; correct template attribute escaping before processing untrusted book data.

## Reference(s):

- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package listing](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [HTML, JSON, Image files, Audio files, Guidance]

**Output Format:** [A self-contained HTML picture book folder with book.json, illustrations, and background music.]

**Output Parameters:** [Variable page count; defaults to 10 story pages.]

**Other Properties Related to Output:** [Portable output uses relative paths for images and audio.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
