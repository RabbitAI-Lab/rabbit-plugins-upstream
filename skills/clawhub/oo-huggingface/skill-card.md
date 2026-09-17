## Description:

Use this skill to handle Hugging Face requests such as searching, reading data, and running supported Hugging Face actions through OOMOL instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search, inspect, and operate Hugging Face models, datasets, Spaces, inference endpoints, embeddings, and chat completions through an OOMOL-connected Hugging Face account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Hugging Face requests are routed through OOMOL's connector data path.

Mitigation: Avoid sending secrets, regulated data, or sensitive prompts unless that connector data path is acceptable for the intended use.

Risk: First-time setup recommends executing remote installer scripts from the shell.

Mitigation: Prefer a verified or package-manager install for the oo CLI, or inspect the installer before execution.

Risk: The security verdict is suspicious because the skill combines a broad third-party connector with remote installer guidance.

Mitigation: Review the skill, connector permissions, and installation path before deployment.

## Reference(s):

- [Hugging Face](https://huggingface.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-huggingface)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, OOMOL sign-in, and an OOMOL-connected Hugging Face account; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
