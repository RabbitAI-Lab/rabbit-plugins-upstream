## Description:

Helps create platform-tailored social-media visuals and captions, with plans for layouts, safe areas, and image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to plan and generate social-media images, thumbnails, and carousels adapted to each platform, with separate on-image copy and captions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation settings, and media supplied for image generation may be sent to dLazy's hosted service.

Mitigation: Review material before submission and avoid sending sensitive or confidential content without authorization.

Risk: Using the service requires an API key, and a global CLI installation persists locally.

Mitigation: Protect the key, rotate or revoke it in the dLazy dashboard when needed, and use npx instead of a global install if persistence is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Image URLs]

**Output Format:** [Markdown with layout plans, copy, status checks, and optional generation commands or image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes platform specifications, safe-area checks, and suggested revisions; image generation uses the dLazy hosted service.]

## Skill Version(s):

1.3.27 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
