## Description:

Pick the right dLazy image model and get it right on the first call. Covers all 22 image tools with their prompt caps, size formats, reference-image support, and credit costs, plus editing and post-processing chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to choose suitable dLazy image-generation and image-editing tools, compose valid CLI commands, check prompt and size limits, and troubleshoot failed or costly image-generation runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and provided local images may be sent to dLazy services, and generated outputs are returned as hosted URLs.

Mitigation: Avoid confidential, regulated, or highly personal prompts and images unless dLazy service use and hosted outputs are acceptable for the workflow and account policy.

Risk: Incorrect model parameters, prompt lengths, or default dimensions can cause failed requests or unwanted image orientation and may waste credits.

Mitigation: Use the skill's model tables, explicit size parameters, and `--dry-run` checks before generation, especially for batch work or user-facing cost estimates.

Risk: Edited or generated images can contain unintended text changes, altered retained elements, artifacts, watermarks, or malformed anatomy.

Mitigation: Review generated images before replacing source assets or delivering final outputs, using the artifact's visual acceptance checklist.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-guide)
- [dLazy homepage](https://dlazy.com)
- [Models quick reference](models.md)
- [Scenario-based model selection](choosing.md)
- [Prompting guide](prompting.md)
- [Editing and post-processing guide](editing.md)
- [Troubleshooting and credit-saving guide](troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline bash commands and parameter tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dLazy CLI commands, dry-run checks, model selection rationale, and image post-processing chains.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
