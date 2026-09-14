## Description:

This skill guides an agent through creating a complete picture book from a theme, including paged story text, style-consistent illustrations, background music, and a self-contained HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to turn a picture-book idea into a portable HTML reading experience with generated illustrations, background music, and page-by-page story text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party CLI and locally saved API credentials.

Mitigation: Install only from trusted dLazy sources, prefer npx or an isolated project-local install, and use an API key that can be rotated or revoked.

Risk: Prompts, parameters, and local reference images may be sent to dLazy services for generation.

Mitigation: Avoid sensitive content in prompts and reference images, and review the service path before using the skill with private material.

Risk: Generated HTML built from untrusted or edited book.json data may execute script through crafted image paths.

Mitigation: Do not open generated books from untrusted book.json files until the template image-path injection issue is fixed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with inline shell commands plus JSON, image, audio, and HTML file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typical generated artifacts include book.json, page and cover images, background music, and index.html.]

## Skill Version(s):

1.3.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
