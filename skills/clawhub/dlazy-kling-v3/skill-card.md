## Description:

Helps agents create Kling V3 videos from text prompts or reference images using dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate videos from text prompts or reference images through the dLazy-hosted Kling V3 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running a third-party npm CLI may expose the local environment to its dependencies.

Mitigation: Review the pinned dLazy CLI before installing; use the on-demand npx invocation if a global install is undesirable.

Risk: API keys saved locally may persist beyond a generation session.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials when persistence is undesirable, and rotate or revoke keys if exposed.

Risk: Prompts and supplied media are sent to dLazy's cloud service, and generation may consume credits.

Mitigation: Submit only content approved for upload and check the cost estimate with dry-run before generating.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Text or Markdown with commands and generated-video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation can return a hosted asset URL or an asynchronous task ID; users may save completed assets locally.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
