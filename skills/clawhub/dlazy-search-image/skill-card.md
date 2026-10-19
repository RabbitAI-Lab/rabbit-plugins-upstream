## Description:

Helps agents search for image assets by keyword and return image URLs and metadata through the dLazy image-search CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, developers, and other agents use this skill to find reference images, backgrounds, and design assets by keyword and receive image URLs and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The description suggests Pixabay search, but using the skill sends prompts and parameters to dLazy services.

Mitigation: Review the service and skill before installing or submitting sensitive search terms.

Risk: Local file paths passed to the CLI may cause files to be uploaded to dLazy media storage.

Mitigation: Avoid supplying local file paths unless uploading those files is intended.

Risk: Using the service requires a dLazy API key.

Mitigation: Store or pass the key securely and avoid exposing it in shared output.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI documentation and source (referenced by skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with image URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image-search results may be returned asynchronously with a task ID.]

## Skill Version(s):

1.3.32 (source: ClawHub release evidence; bundled skill frontmatter states 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
