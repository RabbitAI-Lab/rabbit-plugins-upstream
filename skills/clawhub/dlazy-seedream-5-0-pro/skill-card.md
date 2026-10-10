## Description:

Generates polished images from text prompts and optional reference images for commercial visuals and brand assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and design teams use this skill to generate images for key visuals, typography-rich compositions, and brand materials from prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media are sent to dLazy's hosted services.

Mitigation: Avoid submitting sensitive prompts or media unless approved for third-party processing.

Risk: The dLazy CLI may save an API key in local configuration.

Mitigation: Protect local credentials and rotate or revoke the key in the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Image results, JSON]

**Output Format:** [JSON with hosted image URLs; optionally downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async requests may return a task ID before images are ready.]

## Skill Version(s):

1.2.23 (source: ClawHub release metadata; bundled skill frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
