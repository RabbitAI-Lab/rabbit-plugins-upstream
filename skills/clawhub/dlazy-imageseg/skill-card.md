## Description:

Image matting tool that separates foreground from background and returns a transparent-background image URL for product images, character cutouts, and composition workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce teams use this skill through an agent to remove image backgrounds and obtain transparent PNG-style outputs for product processing, people cutouts, and image composition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input images or local media paths provided to the skill may be uploaded to dLazy's cloud service for processing.

Mitigation: Use the skill only with images approved for external cloud processing, and avoid submitting confidential or regulated media unless dLazy's service terms satisfy the deployment requirements.

Risk: Generated output URLs are hosted by dLazy.

Mitigation: Treat returned URLs as externally hosted assets and download or store outputs according to the user's data handling policy.

Risk: Authentication can store a dLazy API key in a local CLI configuration file.

Mitigation: Use the DLAZY_API_KEY environment variable for ephemeral credentials when local key persistence is not acceptable, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on a pinned third-party npm CLI package.

Mitigation: Review the pinned @dlazy/cli package and declared source before installation in environments with supply-chain review requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI source declared in metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package declared in metadata](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage declared in metadata](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; the dLazy CLI returns JSON containing image output URLs and can save result files locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; local image paths may be uploaded to dLazy media storage, generated outputs are hosted by dLazy, and async runs can return a generateId for polling.]

## Skill Version(s):

1.3.20 (source: server release evidence; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
