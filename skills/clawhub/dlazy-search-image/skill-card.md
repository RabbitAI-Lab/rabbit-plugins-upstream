## Description:

Searches for images by keyword through dLazy and returns image URLs and metadata for reference and design use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and content creators use this skill to find image URLs and metadata for references, backgrounds, and design assets via the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the dLazy cloud service rather than only a direct Pixabay search.

Mitigation: Review dLazy's service terms and data handling before sending search queries or parameters.

Risk: Authentication uses a dLazy API key, and the skill installs an external npm CLI.

Mitigation: Protect the API key and review the pinned @dlazy/cli@1.2.3 package before installing.

Risk: Local file-path inputs can upload media, and --save can download results to disk.

Mitigation: Avoid local file paths and --save unless the upload or download is intentional.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Image URLs, Image metadata]

**Output Format:** [JSON response with image results or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local asset download with --save.]

## Skill Version(s):

1.3.27 (source: ClawHub release evidence; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
