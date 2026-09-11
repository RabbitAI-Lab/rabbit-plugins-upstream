## Description:

Use when installing the full Pruna generative media suite: guides, tools, and workflows in one package.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to install the complete Pruna generative media suite and make its image, video, audio, and workflow skills available to an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install command is unpinned and can add a changing set of dependent skills.

Mitigation: Use a pinned commit or reviewed release, then review the dependent skills before granting broad filesystem, network, or command access.

Risk: Media-generation workflows may run while API credentials are available in the environment.

Mitigation: Expose only the required credentials for the current task and avoid running the skill with unrelated secrets in the environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/pruna)
- [Pruna dashboard](https://dashboard.pruna.ai/)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Installation guidance for a suite of dependent skills; downstream tools may require PRUNA_API_KEY, REPLICATE_API_TOKEN, curl, ffmpeg, and ffprobe.]

## Skill Version(s):

1.0.12 (source: server release metadata, artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
