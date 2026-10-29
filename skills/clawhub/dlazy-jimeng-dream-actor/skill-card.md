## Description:

Convert static character images into vivid action videos with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use the skill to turn a character image into an action video by providing a prompt and image to Jimeng Dream Actor.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy for generation, and generated media is hosted by its service.

Mitigation: Use only media you are comfortable uploading and review dLazy's service terms.

Risk: Generation may incur account charges, and login stores an API key in the local CLI configuration.

Mitigation: Account for generation costs, review the pinned CLI before installation, and use the documented DLAZY_API_KEY environment variable if you prefer not to save the key locally.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Structured JSON response with a generated media URL; optionally a media file saved locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a prompt and up to one image and one video; asynchronous task IDs can be returned when waiting is disabled.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
