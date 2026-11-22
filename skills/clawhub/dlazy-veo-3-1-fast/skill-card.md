## Description:

Fast response and generation of short videos with Google Veo 3.1 Fast.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate short videos from text prompts or supplied images, or to extend an existing video, through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial, and some CLI and runtime references could not be resolved, leaving parts of the workflow unreviewed.

Mitigation: Review the unresolved CLI and runtime details and inspect the pinned CLI package before installing if full workflow assurance is needed.

Risk: Prompts and any local image or video files supplied to the skill are sent to dLazy's hosted service for processing.

Mitigation: Check prompts and media for sensitive or unauthorized content before submitting them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI source repository (listed in skill metadata; server import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Hosted video asset URLs and a JSON result or asynchronous task status envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Short generated or extended video; supplied prompts and local media are sent to the hosted service, and generated assets are hosted by dLazy.]

## Skill Version(s):

1.3.41 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
