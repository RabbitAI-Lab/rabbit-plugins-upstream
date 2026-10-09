## Description:

Enhances low-resolution images and returns a URL for the upscaled result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to enhance low-resolution images through dLazy's hosted super-resolution service and retrieve the enhanced image URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images supplied for enhancement are uploaded to dLazy's hosted service.

Mitigation: Do not submit sensitive images unless their upload to dLazy is acceptable.

Risk: Installing the CLI and saving an API key creates third-party software and credential exposure.

Mitigation: Confirm trust in the dLazy package and service; consider on-demand npx use and a per-invocation API key instead of a global install or saved key.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown instructions and JSON response with an enhanced image URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save the enhanced image locally or return an asynchronous task ID.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
