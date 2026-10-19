## Description:

Guides creation of a consistent digital lecturer for landscape courses using portrait recipes, narration, and a slide-first video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Course creators, trainers, and educators use this skill to plan and produce lessons with a reusable AI lecturer, voiceover, and slide-led video segments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running the DLazy CLI executes third-party commands.

Mitigation: Review the npm install command and generated commands before running them.

Risk: DLazy authentication uses an API key stored locally or supplied through the environment.

Mitigation: Protect the API key and review how it is stored or passed to the CLI.

Risk: Generation calls spend provider credits, and selected course files may be uploaded to DLazy services.

Mitigation: Review expected costs and approve files before paid calls or --files uploads.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-course-avatar)
- [DLazy homepage](https://dlazy.com)
- [Course video pipeline](artifact/pipeline.md)
- [Portrait and slide recipes](artifact/recipes.md)
- [Troubleshooting and publishing guidance](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans portrait, audio, and slide production; media generation requires external tools and provider credits.]

## Skill Version(s):

1.0.22 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
