## Description:

Runs registered ComfyUI workflows for image, video, music, and speech generation, editing, matting, face animation, and voice cloning on a local or trusted server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miemieeeee](https://clawhub.ai/user/miemieeeee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users direct an agent to choose and run reviewed ComfyUI workflows, check server readiness, and import their own workflows after review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice cloning and face animation can be used without the subject's consent or for impersonation.

Mitigation: Use these features only with clear rights and consent from the people whose voice, face, or likeness is used.

Risk: Untrusted servers or unreviewed workflow imports may expose inputs or run unwanted operations.

Mitigation: Connect only to local or trusted ComfyUI servers and review imported workflow templates before activation.

Risk: Prompts, media paths, outputs, job metadata, and optional server settings may remain in per-user storage.

Mitigation: Review the local data directory and avoid submitting sensitive media or prompts without appropriate safeguards.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/miemieeeee/skills/comfyui-agent-skill-mie)
- [Workflow selection and capabilities](references/workflows.md)
- [CLI contract](references/cli.md)
- [Workflow extension guide](references/extension.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report saved media paths, job status, and diagnostic errors.]

## Skill Version(s):

1.0.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
