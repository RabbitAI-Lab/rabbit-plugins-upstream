## Description:

Guides creators through defining consistent characters and hero props for AI video, from passports and reference sheets to expressions, voice, shot prompts, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to define characters and hero props consistently across AI-generated video shots, then prepare and check reference sheets, expressions, voices, and prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled screenshot renderer can expose local files and uses unrestricted cross-origin access.

Mitigation: Restrict reads to approved assets, bind the renderer to loopback, and remove unrestricted CORS before use.

Risk: Optional dependencies and Blender configuration changes can affect the local environment.

Mitigation: Review and pin optional dependencies, and approve Blender configuration changes separately.

Risk: Cloud image and voice services receive submitted assets and recordings.

Mitigation: Use those services only with assets and recordings authorized for the providers.

Risk: Preparing blinded judging copies can affect the originals.

Mitigation: Preserve originals when preparing blinded judging copies.

Risk: The skill includes face-filter bypass advice.

Mitigation: Avoid the face-filter bypass advice.

## Reference(s):

- [Character Passport release on ClawHub](https://clawhub.ai/vargai/skills/character-passport)
- [Passport writing guide](artifact/references/passport.md)
- [Turnaround and expression sheets guide](artifact/references/sheets.md)
- [Acting and expression guide](artifact/references/acting.md)
- [Voice design guide](artifact/references/voice.md)
- [Code routes guide](artifact/references/code.md)
- [Character consistency test write-up](https://claude.ai/artifact/AJ1g4Qren3ZvwERSwrQigt)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Images, Audio, Code, Shell commands]

**Output Format:** [Markdown files, image and audio assets, code files, and command-line prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-specific character and prop references, prompt text, and validation results; optional generated media may use external services.]

## Skill Version(s):

1.0.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
