## Description:

Generates videos from a first-frame image and a text prompt using Jimeng through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short image-to-video generations from a first-frame image and a text prompt through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external npm CLI runs locally and can be installed globally.

Mitigation: Review the pinned CLI package before installation or use the documented npx option instead of a global install.

Risk: The service requires an API key that the CLI may save in a local configuration file.

Mitigation: Protect the local configuration and use a per-invocation key where persistent storage is unsuitable.

Risk: Prompts and user-supplied media are sent to dLazy-hosted services for generation.

Mitigation: Only submit content approved for external processing.

Risk: The examples disagree about the image flag and show an image result for a video workflow.

Mitigation: Check the CLI help and confirm the returned asset type before relying on the examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON results, Video links]

**Output Format:** [Markdown instructions and JSON CLI responses containing hosted result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may first return a task ID; the CLI can download the completed asset to a local path.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata; artifact frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
