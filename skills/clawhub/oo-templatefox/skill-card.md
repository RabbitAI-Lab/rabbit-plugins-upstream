## Description:

TemplateFox (templatefox.com). Use this skill for ANY TemplateFox request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate TemplateFox through an OOMOL-connected account, including generating images or PDFs, inspecting templates, checking account credits, and performing PDF utilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that could be risky if run automatically or without review.

Mitigation: Install the oo CLI through a trusted, reviewable method and require user review before running installer commands.

Risk: Write actions can generate assets or merge PDFs using user-provided payloads.

Mitigation: Confirm the exact action, payload, and expected effect with the user before running write actions.

## Reference(s):

- [TemplateFox homepage](https://templatefox.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-templatefox)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return signed download URLs and execution metadata from TemplateFox connector actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
