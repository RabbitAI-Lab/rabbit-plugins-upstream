## Description:

Generate realistic digital human broadcast videos from portrait images and audio or text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate digital human broadcast videos from a portrait and audio or text prompts with Jimeng OmniHuman 1.5.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portraits, audio, and prompts are sent to dLazy services for generation.

Mitigation: Submit only media and prompts approved for external processing, and review the service privacy terms.

Risk: Use requires a paid API account and a locally stored API key.

Mitigation: Review generation costs, protect the API key, and rotate or revoke it if exposed.

Risk: The skill's declared CLI package is installed or run through npm/npx.

Mitigation: Review the pinned CLI package before installing or running it.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [Hosted video asset URL and JSON generation response; a video file can be downloaded when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may return an asynchronous task identifier when requested; completed assets are hosted by the service.]

## Skill Version(s):

1.3.35 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
