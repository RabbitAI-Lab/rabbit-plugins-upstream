## Description:

Generates 1MP raster images from text prompts through dLazy's Recraft V4 integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate and iterate on 1MP raster images from text prompts, with optional local download of results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied files may be uploaded to dLazy, and generated assets are hosted by dLazy.

Mitigation: Send only prompts and files you intend to share with the service.

Risk: Authentication may save an API key in the local CLI configuration.

Mitigation: Use a per-invocation DLAZY_API_KEY if local key persistence is undesirable; rotate or revoke keys as needed.

Risk: Installing the third-party CLI adds executable software to the environment.

Mitigation: Review the package before use and prefer the pinned npx @dlazy/cli@1.2.3 command if you do not want a persistent global installation.

## Reference(s):

- [dLazy CLI repository (package metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell commands and JSON image-result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns hosted image URLs; results can optionally be downloaded to a local file.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
