## Description:

Generate cinematic videos with Google Veo 3.1 from text prompts, images, and existing video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and developers can generate cinematic videos from prompts, guide generation with images, or extend an existing video using dLazy's Veo 3.1 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media inputs are sent or uploaded to dLazy's hosted service.

Mitigation: Submit only prompts and media you are comfortable sharing with that service.

Risk: Video generation may consume paid credits.

Mitigation: Use --dry-run to preview the request and estimated cost before generation.

Risk: The CLI stores an API key in local configuration or accepts it through an environment variable.

Mitigation: Keep the API key private and rotate or revoke it from the dLazy dashboard if needed.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video files, JSON generation status and result metadata]

**Output Format:** [Hosted video URL or saved video file, with JSON status and result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation can run asynchronously with --no-wait.]

## Skill Version(s):

1.3.34 (source: server-resolved release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
