## Description:

Helps agents generate short videos from text or image prompts, or extend a video, using Google Veo 3.1 Fast through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short text-to-video or image-to-video clips and video extensions through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected media may be sent to dLazy's cloud service, and generated results are hosted there.

Mitigation: Share only media and prompts you are comfortable uploading to dLazy.

Risk: An API key may be stored in local CLI configuration.

Mitigation: Protect the local account and rotate or revoke the key if exposed.

Risk: Generation may consume paid credits.

Mitigation: Check the cost estimate with the available dry-run option before generating.

Risk: Installing the third-party CLI runs publisher-provided software.

Mitigation: Review the pinned npm CLI source before using the global install path.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI source (publisher-provided link; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown instructions and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include hosted media URLs or an asynchronous task ID; the CLI can optionally save media locally.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata; bundled frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
