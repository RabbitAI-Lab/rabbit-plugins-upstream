## Description:

Routes image, video, and audio generation requests to the appropriate dLazy CLI model based on user intent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to ask an agent to select and run dLazy CLI commands for image, video, and audio generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation may cause ordinary generation requests to use the dLazy service and incur external API usage.

Mitigation: Install only when dLazy should handle these generation workflows, and confirm the selected dLazy command before execution when cost or routing matters.

Risk: Persistent API-key storage can expose organization credentials on shared or temporary machines.

Mitigation: Prefer per-run DLAZY_API_KEY or a managed secret in shared environments, and rotate or revoke the key after use when exposure is possible.

Risk: Image, video, or audio file inputs may be uploaded to dLazy media storage for processing.

Mitigation: Confirm before sending local media files and avoid uploading sensitive or restricted assets unless the user has approved that disclosure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands; dLazy CLI invocations return JSON envelopes and hosted media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use local media paths as inputs and return generated media URLs hosted by dLazy.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
