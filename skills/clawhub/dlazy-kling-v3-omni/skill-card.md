## Description:

Generates Kling V3 Omni videos from prompts and optional reference images or video through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate short videos from text prompts and optional images or reference video, with links to hosted results or a saved local asset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be sent to dLazy's cloud service, where generated assets are hosted.

Mitigation: Avoid sharing private media unless the service terms and hosting arrangements meet your requirements.

Risk: Login can store an API key in local CLI configuration.

Mitigation: Protect the local credential and rotate or revoke it if exposed.

Risk: Running the third-party dLazy CLI introduces package supply-chain exposure.

Mitigation: Review the pinned CLI source and package before installing if supply-chain assurance is required.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Text guidance and JSON generation results with hosted asset URLs; optional locally saved media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID before the media is ready.]

## Skill Version(s):

1.3.26 (source: ClawHub release; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
