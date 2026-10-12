## Description:

Searches for image assets by keyword through the dLazy CLI and returns image URLs and metadata for references and design work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and other users can search for reference images, backgrounds, and design assets by keyword and use returned image links and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The image-search description may obscure that requests use a third-party dLazy service and require an account and API key.

Mitigation: Review the dLazy CLI and service terms before installing; use a dedicated, revocable key and protect it from disclosure.

Risk: Search prompts and parameters are sent to dLazy endpoints, and local file paths may cause uploads.

Mitigation: Avoid sensitive prompts and do not pass local file paths unless the intended files may be uploaded.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Image URLs and metadata]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID instead of immediate results; optional asset download is supported.]

## Skill Version(s):

1.3.29 (source: ClawHub release; bundled skill frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
