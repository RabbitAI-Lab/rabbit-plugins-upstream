## Description:

Tongyi Wanxiang Wan 2.7 supports text-to-video, first/last-frame video generation, and reference image or video to video generation through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to call Wan 2.7 through the dLazy CLI for text-to-video, first/last-frame, and reference-based video generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an external npm CLI dependency and dLazy hosted service for generation.

Mitigation: Install only if you trust the dLazy CLI and service; prefer npx or a non-privileged install and review the linked source or package in sensitive environments.

Risk: Prompts and media files supplied to image, video, or audio parameters are sent to dLazy service endpoints for processing.

Mitigation: Only submit media and prompts that are acceptable to upload to dLazy, and avoid sending confidential material unless your organization has approved that service use.

Risk: The dLazy API key is used for authenticated requests and may be saved in the local CLI configuration.

Mitigation: Use a revocable API key, keep it scoped to the intended organization, and rotate or revoke it from the dLazy dashboard when access changes.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON responses containing generated media URLs or task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets may be returned as hosted URLs or downloaded to a local path when the save option is used.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
