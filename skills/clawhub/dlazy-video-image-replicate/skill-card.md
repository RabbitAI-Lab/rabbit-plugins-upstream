## Description:

Helps recreate the look and structure of a reference image or video using the user's own subjects, products, or characters through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to request image or video recreations based on a reference while substituting their own subjects or products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached media are sent to dLazy's hosted service, and attached local files are uploaded.

Mitigation: Review prompts and files before sharing them with the service; avoid attaching sensitive material.

Risk: The CLI may save an API key in local configuration.

Mitigation: Protect the local config and rotate or revoke the key if exposed.

Risk: Project sessions retain context across follow-up requests.

Mitigation: Start a new project for unrelated work and clear sessions when needed.

Risk: A global CLI installation persists on the user's machine.

Mitigation: Prefer the pinned npx invocation if a global installation is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Text with CLI commands and streamed agent responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped, multi-turn responses; reference files may be attached.]

## Skill Version(s):

1.3.25 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
