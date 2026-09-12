## Description:

Happy Horse 1.0 is a dLazy video-generation skill that routes text-to-video, first-frame-to-video, reference-to-video, and video-editing requests to the matching hosted model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and content creators use this skill to generate or edit short videos through the dLazy Happy Horse 1.0 CLI workflow. It supports text prompts, first-frame images, reference images, and video-editing inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party CLI and requires authentication with a dLazy API key.

Mitigation: Review the dLazy CLI package before installation in sensitive environments, prefer the pinned npx invocation when avoiding a persistent global binary, and treat the API key as a credential that may need rotation or revocation.

Risk: Prompts, parameters, and local media paths supplied to image, video, or audio fields are sent to dLazy-hosted services.

Mitigation: Only submit prompts and media files that are appropriate to upload to dLazy, and review applicable service terms before using sensitive data.

Risk: Cloud generation can fail because of authentication, account balance, policy, or asynchronous task errors.

Mitigation: Check returned error codes and task status before using outputs downstream, and use dry-run or no-wait modes when estimating cost or managing long-running jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Text, Files]

**Output Format:** [JSON responses with generated media URLs; optional saved media files when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns an asynchronous task ID when --no-wait is used; generated assets are hosted on files.dlazy.com.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
