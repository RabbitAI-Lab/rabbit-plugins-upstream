## Description:

Creates a short product motion film from a public project website or GitHub repository, with a sourced brief, storyboard, MP4, and editable project files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dktrn9ne](https://clawhub.ai/user/dktrn9ne)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and product teams use this skill to turn a public product link into a sourced, seven-scene launch film with original sound and editable assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project links and site content are fetched over the network; font setup downloads Google-hosted files.

Mitigation: Provide only public project URLs and approve network access to the project site, GitHub, and font hosts.

Risk: Generated assets may include inaccurate product claims or unlabeled illustrative values.

Mitigation: Check claims, numbers, availability, branding, and the final export against the current source before sharing.

Risk: Rendering creates files and starter dependencies are specified as version ranges.

Mitigation: Start with an empty output directory, inspect generated files, and pin dependencies more tightly when reproducibility matters.

## Reference(s):

- [Bravado skill release](https://clawhub.ai/dktrn9ne/skills/bravado)
- [Bravado workflow](references/workflow.md)
- [Bravado quality bar](references/quality-bar.md)

## Skill Output:

**Output Type(s):** [Video files, Markdown, Code, Configuration, Guidance]

**Output Format:** [MP4 video with a source brief, storyboard, editable Python and JSON project files, and a written delivery summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default render target is 1920×1080 at 30 fps; source claims and illustrative metrics require review before publication.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
