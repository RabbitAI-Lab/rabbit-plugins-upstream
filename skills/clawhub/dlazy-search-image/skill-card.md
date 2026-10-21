## Description:

Searches for image assets by keyword and returns image URLs and metadata for visual references and design work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, developers, and other users can search for image URLs and metadata to find references, backgrounds, and design assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image searches use a third-party service and require a dLazy API key stored locally.

Mitigation: Use only if the dLazy service boundary is acceptable; protect and rotate the API key as needed.

Risk: Providing local media paths may upload files to dLazy infrastructure.

Mitigation: Do not provide local media paths unless upload is intended.

Risk: The image-search description conflicts with parts of the documentation about generation and uploads.

Mitigation: Review the CLI package and command behavior before installing or running it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package listed in skill metadata](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON with image URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task identifier instead of immediate results.]

## Skill Version(s):

1.3.33 (source: ClawHub release evidence; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
