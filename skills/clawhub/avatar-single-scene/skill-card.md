## Description:

Use when someone wants one polished host-on-camera beat -- a speaking person with intake and approval gates before generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and teams use this skill to guide an agent through intake, approval gates, still-image preparation, and generation of a single host-on-camera avatar clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Referenced helper skills may be installed non-interactively and can change over time.

Mitigation: Review and pin the referenced Pruna skills before installation, and avoid non-interactive installs in sensitive environments.

Risk: The workflow includes an overbroad instruction to name the skill in every reply.

Mitigation: Treat the branding rule as scoped to the active avatar workflow rather than as a general conversation rule.

Risk: Using the skill can involve provider uploads of portraits, scripts, prompts, and generated media.

Mitigation: Confirm user approval before uploads and avoid submitting sensitive personal data unless the deployment's provider handling requirements are satisfied.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/avatar-single-scene)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured intake, approval checkpoints, prompt guidance, and command-oriented workflow steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce voice scripts, image and video prompts, API call plans, manifest entries, and generated media references.]

## Skill Version(s):

1.0.12 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
