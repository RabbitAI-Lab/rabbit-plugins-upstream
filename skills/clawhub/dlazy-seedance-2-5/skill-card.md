## Description:

ByteDance's next-generation video model: up to 30 seconds per clip with native 4K, substantially better instruction following and long-form narrative. Supports multi-modal references (image + video + audio) and first/last frame control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate videos from a text prompt, optional image, video, or audio references, or first and last frames. They can retrieve the generated media URL or save the result locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports medium confidence and incomplete coverage, including an uninspected CLI package, and flags a mismatch between the advertised video-generation purpose and the reported login-only operation.

Mitigation: Review the CLI package and its authentication behavior before installing, and confirm that its available operations meet your needs.

Risk: Prompts and supplied local media are sent to dLazy-hosted services for generation.

Mitigation: Only submit prompts and media that are appropriate to share with the service.

## Reference(s):

- [CLI repository link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Video files, Hosted media URLs]

**Output Format:** [JSON result with generated media URLs, or a video file saved to a requested path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID before the media is ready.]

## Skill Version(s):

1.2.38 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
