## Description:

Creates labeled vertical AI-generated UGC ads with a consistent creator, product, and script across shots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers and creative teams use the skill to plan and generate short product ads featuring an AI creator, including scripts, shot prompts, editing guidance, and AI disclosure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer is unpinned, so a later install could retrieve changed content.

Mitigation: Install from a reviewed, pinned release or commit and check the source before updating.

Risk: Product images and other supplied creative material may be sent to external generation services.

Mitigation: Send only material approved for external processing, and review the provider's data handling terms first.

Risk: The security scan did not resolve one local reference, leaving its coverage incomplete.

Mitigation: Inspect the unresolved reference and review the complete skill contents before installation.

## Reference(s):

- [Prompt examples](artifact/references/prompts.md)
- [ClawHub release](https://clawhub.ai/vargai/skills/ai-ugc-ad-video)
- [Varg AI UGC ad guide](https://varg.ai/how-to/make-a-ugc-ad-video)

## Skill Output:

**Output Type(s):** [Video, Text, Prompts, Shell commands]

**Output Format:** [Timed scripts and shot prompts; labeled vertical MP4 video, typically 9:16 at 1080×1920]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation model and retakes affect the final video and cost.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
