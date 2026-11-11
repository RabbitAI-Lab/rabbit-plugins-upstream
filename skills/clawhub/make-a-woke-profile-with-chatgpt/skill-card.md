## Description:

Turn a selfie into a satirical profile set of AI-generated images, animated tiles, and a shareable collage using GPT Image through Varg or prompts in ChatGPT.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can turn a selfie they own or have clear permission to use into a satirical image set, animated collage, and optional presenter video. They can run the Varg scripts or use the prompt guide in ChatGPT.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends selfies and related data to external services.

Mitigation: Use only your own photo or one you have clear permission to use, and review how the services handle submitted images and data.

Risk: The security evidence reports deletion of existing output files.

Mitigation: Review the output directory and back up any files there before running the skill.

Risk: The security evidence flags unpinned install commands and notes that presenter.py was only partially inspected.

Mitigation: Review the install commands and inspect presenter.py and other components before installing dependencies or running the presenter workflow.

## Reference(s):

- [Varg how-to guide](https://varg.ai/how-to)
- [ClawHub skill release](https://clawhub.ai/vargai/skills/make-a-woke-profile-with-chatgpt)
- [Prompt guide](artifact/references/prompts.md)

## Skill Output:

**Output Type(s):** [Files, Guidance]

**Output Format:** [PNG/JPG images, GIFs, MP4 video, and Markdown prompt guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Eleven satirical image tiles, a 4:5 collage, and optional animated or presenter-mode video.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
