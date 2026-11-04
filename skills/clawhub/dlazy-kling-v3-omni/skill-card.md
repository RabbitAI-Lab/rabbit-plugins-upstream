## Description:

Generates videos with Kling v3 Omni from prompts and optional image or video references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate short videos from text prompts and optional image or video references, with controls for aspect ratio, duration, sound, and generation mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompt and reference media are sent to dLazy, and local media files may be uploaded for generation.

Mitigation: Submit only prompts and media you are comfortable sharing with dLazy.

Risk: Video generation may incur account charges.

Mitigation: Use --dry-run to preview the request and cost estimate before generating.

Risk: The CLI stores an API key in the user's local configuration, and the external CLI executable and dependencies are outside the reviewed artifact.

Mitigation: Protect the local configuration, install the CLI from a trusted source, and rotate or revoke the API key if exposed.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Hosted video assets with a JSON response containing output URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are hosted by dLazy; asynchronous requests can return a task identifier before outputs are ready.]

## Skill Version(s):

1.3.36 (source: server release evidence; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
