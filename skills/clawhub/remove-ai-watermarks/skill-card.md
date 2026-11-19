## Description:

Removes and identifies AI watermarks and provenance marks in images, video, audio, and text the user generated or edited. Covers Gemini sparkles, SynthID, Microsoft InvisMark, Meta Content Seal, C2PA, EXIF/XMP/IPTC metadata, compatible public AudioSeal/WavMark/Perth v1/SilentCipher audio, and Sora/Veo/Seedance/Doubao/Dola/Hailuo/Vidu/Kling and Wan labels. Use when the user wants to strip or clean AI watermarks and generation labels, or asks whether a file was AI-generated or carries AI provenance, even if they do not name remove-ai-watermarks. Do not use for stock-agency, marketplace, classifieds, or other third-party paid-asset watermarks.

This skill is for research and development only.

## Publisher:

[wiltodelta](https://clawhub.ai/user/wiltodelta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use the skill to inspect eligible images, video, audio, and text for supported AI labels or provenance marks, and to remove supported marks from content they generated or edited when permitted.

### Deployment Geography for Use:

Global, subject to local restrictions on removing AI labels.

## Known Risks and Mitigations:

Risk: Tool scope is unclear, and the bundled probe invokes external commands.

Mitigation: Review the commands and targets before running them, and grant only the command permissions needed for the requested task.

Risk: Removal is limited to content the user generated or edited and is subject to local restrictions; third-party paid-asset marks are out of scope.

Mitigation: Confirm the user may change the content, follow applicable local restrictions, and refuse removal from protected third-party assets.

Risk: A missing detected mark does not prove a file is clean, human-made, or free of server-side generation history.

Mitigation: Report only the signals and command results observed; do not claim a clean or human-made origin.

## Reference(s):

- [ClawHub release](https://clawhub.ai/wiltodelta/skills/remove-ai-watermarks)
- [Project homepage](https://raiw.cc)
- [Project repository (metadata link)](https://github.com/wiltodelta/remove-ai-watermarks)
- [Python API guide](https://github.com/wiltodelta/remove-ai-watermarks/blob/main/docs/python-api.md)
- [Command reference](references/commands.md)
- [Installation guide](references/install.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, Files]

**Output Format:** [Markdown guidance, shell commands, and CLI-generated text or JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce cleaned media or text files when a supported removal is requested; available operations depend on installed extras and hardware.]

## Skill Version(s):

1.0.21 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
