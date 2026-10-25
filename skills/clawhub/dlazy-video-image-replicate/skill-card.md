## Description:

Analyzes a user-provided reference image or video and recreates its look and structure with the user's own subject, product, or characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to recreate the visual style or structure of a reference image or video with their own subject, product, or characters through dLazy's hosted agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference media are sent to dLazy services, so sensitive content may be subject to the provider's privacy and retention practices.

Mitigation: Review dLazy's privacy and retention terms and avoid uploading sensitive media unless authorized.

Risk: The skill uses a saved organization API key, project-scoped sessions, and service credits.

Mitigation: Protect the API key, confirm the intended project before follow-ups, and account for service-credit usage.

## Reference(s):

- [dLazy service website](https://dlazy.com)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)

## Skill Output:

**Output Type(s):** [Text, Images, Videos]

**Output Format:** [Streaming agent responses with image or video deliverables where supported]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped sessions; selected reference files are uploaded to dLazy media storage.]

## Skill Version(s):

1.3.33 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
