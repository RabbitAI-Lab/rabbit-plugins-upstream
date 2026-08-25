## Description:

Creates interactive Wallpaper Engine Web wallpapers with music playback, album navigation, synchronized LRC lyrics, theming, settings, localization, performance modes, and visible credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhilogic-oss](https://clawhub.ai/user/zhilogic-oss)

### License/Terms of Use:

Apache 2.0

## Use Case:

External users, creators, and developers use this skill to collaborate with an agent on Wallpaper Engine music Web wallpapers built from authorized audio, artwork, lyrics, and source records. It supports staged asset review, catalog construction, player implementation, interface refinement, testing, and release attribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated wallpapers may include music, lyrics, covers, logos, fonts, trademarks, or other materials that are not authorized for the user's intended use.

Mitigation: Require user-provided or rights-holder-authorized assets, record material sources and permission status, and keep visible credits in the wallpaper before release.

Risk: A wallpaper can appear functional in a normal browser while audio, property callbacks, localization, visualizers, or performance behave differently in Wallpaper Engine.

Mitigation: Run the bundled validation workflow and test the actual Wallpaper Engine build across playback, lyrics, properties, resolutions, and performance modes.

Risk: Published wallpapers may fail for subscribers if they reference absolute paths or source folders on the creator's computer.

Mitigation: Copy selected release assets into the wallpaper project, use stable project-relative paths, and validate catalog references before delivery.

Risk: Tool credits or interface references may be mistaken for wallpaper authorship or permission to use third-party material.

Mitigation: Keep the actual wallpaper author distinct, show the tool credit discreetly, include OriginalCube inspiration only when applicable, and state that attribution does not grant rights.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/zhilogic-oss/create-music-web-wallpaper)
- [Wallpaper Engine Web wallpaper notes](references/wallpaper-engine-web.md)
- [Catalog and asset workflow](references/catalog-and-assets.md)
- [Lyrics behavior](references/lyrics.md)
- [Credits and rights](references/credits-and-rights.md)
- [Acceptance checklist](references/acceptance.md)
- [Wallpaper Engine Web overview](https://docs.wallpaperengine.io/en/web/overview.html)
- [OriginalCube Bocchi the Rock album-player wallpaper reference](https://steamcommunity.com/sharedfiles/filedetails/?id=2905017768)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and generated HTML, CSS, JavaScript, JSON, and metadata files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update local Wallpaper Engine Web wallpaper project files and validation reports.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
