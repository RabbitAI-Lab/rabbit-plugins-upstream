## Description:

Mysteries Prep automates a Farsight media preparation workflow that transcribes audio, cross-checks target information, generates image prompts and images, and prepares a DaVinci Resolve timeline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and media-production agents use this skill to prepare Farsight Mysteries projects from source audio and a target information sheet into transcript-aligned image assets and DaVinci Resolve timeline updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify the currently open DaVinci Resolve project.

Mitigation: Run it only on a duplicate or backed-up project and require explicit confirmation before timeline or media-pool changes.

Risk: The skill reads local audio and target files and creates folders and generated images beside the provided media.

Mitigation: Provide exact approved paths, review proposed output locations, and confirm before file creation or media generation.

Risk: The artifact includes safety-filter bypass wording for image prompts.

Mitigation: Do not allow safety-filter workarounds; require compliant prompt rewrites and human review for blocked content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/mysteries-prep)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with local paths, generated prompts, image files, and DaVinci Resolve Python API actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates timestamped media-prep artifacts and may modify the currently open DaVinci Resolve project.]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
