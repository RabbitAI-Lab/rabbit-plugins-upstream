## Description:

Removes and identifies AI watermarks and provenance marks in images and video the user generated or edited. Covers Gemini sparkles, SynthID, Microsoft InvisMark, Meta Content Seal, C2PA, EXIF/XMP/IPTC metadata, and Sora/Veo/Seedance/Doubao/Dola/Hailuo/Vidu/Kling and Wan labels. Use when the user wants to strip or clean AI watermarks and generation labels, or asks whether a file was AI-generated or carries AI provenance, even if they do not name remove-ai-watermarks. Do not use for stock-agency, marketplace, classifieds, or other third-party paid-asset watermarks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wiltodelta](https://clawhub.ai/user/wiltodelta)

### License/Terms of Use:

Apache 2.0

## Use Case:

External users and developers use this skill to inspect or edit AI marks and provenance in image and video files they are authorized to change. It guides identification, metadata checks, and targeted removal while excluding marks that protect third-party paid assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Removing marks or metadata can discard provenance information or alter image quality.

Mitigation: Keep the original file and review the edited result.

Risk: Uploading media to the optional hosted service may expose it to that service's privacy practices.

Mitigation: Review the service's privacy terms before sharing files.

Risk: Editing media without authorization or removing marks that protect third-party paid assets can cause harm.

Mitigation: Use the workflow only on media the user is authorized to edit; refuse third-party paid-asset watermark removal.

## Reference(s):

- [Command reference](references/commands.md)
- [Installation guide](references/install.md)
- [raiw.cc hosted service](https://raiw.cc)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown guidance with shell commands and status reporting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses command exit codes and confirmed output paths; media output depends on the selected operation.]

## Skill Version(s):

1.0.15 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
