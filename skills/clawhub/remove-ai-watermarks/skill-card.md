## Description:

Removes and identifies AI watermarks and provenance marks in user-owned images and video, including visible labels, SynthID, InvisMark, Content Seal, C2PA, and EXIF/XMP/IPTC metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wiltodelta](https://clawhub.ai/user/wiltodelta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect user-owned generated or edited media for AI provenance signals and run the remove-ai-watermarks CLI to strip selected marks with explicit output paths. It is not for removing stock-agency, marketplace, classifieds, or other third-party paid-asset marks or for making deceptive origin claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading the remove-ai-watermarks package could execute third-party package code from a publisher the user does not trust.

Mitigation: Install only after confirming trust in the package publisher and package source.

Risk: Image metadata removal can overwrite the source file when no output path is provided.

Mitigation: Use explicit output paths and keep originals when provenance or reversibility matters.

Risk: The skill could be misused to remove marks from third-party paid assets or to misrepresent AI-generated content as human-made.

Mitigation: Apply the skill only to user-owned media and refuse third-party paid-asset watermark removal or deceptive origin claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wiltodelta/skills/remove-ai-watermarks)
- [Project homepage](https://raiw.cc)
- [Repository](https://github.com/wiltodelta/remove-ai-watermarks)
- [Command recipes](references/commands.md)
- [Install extras](references/install.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON probe output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses explicit output paths for write commands and reports only command results observed in the session.]

## Skill Version(s):

1.0.5 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
