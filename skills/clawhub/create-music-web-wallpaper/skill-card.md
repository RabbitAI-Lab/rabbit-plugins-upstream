## Description:

Create, rebuild, or refine interactive music and album-player wallpapers for Wallpaper Engine using HTML, CSS, and JavaScript.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhilogic-oss](https://clawhub.ai/user/zhilogic-oss)

### License/Terms of Use:

Apache 2.0

## Use Case:

External users, creators, and developers use this skill to collaborate with an agent on Wallpaper Engine web wallpapers that include music playback, album or track navigation, synchronized LRC lyrics, themes, settings, localization, credits, and release checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated wallpapers may include copyrighted music, lyrics, artwork, logos, fonts, or other third-party material without sufficient rights.

Mitigation: Use user-provided or otherwise authorized assets, record creator and permission details for every material, and do not treat attribution as permission.

Risk: Generated wallpapers are expected to retain a discreet visible tool credit with the skill author's name and email.

Mitigation: Install and use the skill only when that visible credit requirement is acceptable for the intended wallpaper release.

Risk: A publishable wallpaper may fail for subscribers if media paths still point to unrelated local folders.

Mitigation: Copy selected media into the wallpaper project, use project-relative catalog paths, and run the bundled validation script before release.

Risk: Browser-only testing may miss Wallpaper Engine playback, property, localization, or visualizer issues.

Mitigation: Test the actual Wallpaper Engine build and use the acceptance checklist before claiming completion.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/zhilogic-oss/create-music-web-wallpaper)
- [Wallpaper Engine Web wallpaper notes](references/wallpaper-engine-web.md)
- [Catalog and asset workflow](references/catalog-and-assets.md)
- [Lyrics behavior](references/lyrics.md)
- [Credits and rights](references/credits-and-rights.md)
- [Acceptance checklist](references/acceptance.md)
- [OriginalCube album-player wallpaper reference](https://steamcommunity.com/sharedfiles/filedetails/?id=2905017768)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands, generated HTML/CSS/JavaScript, JSON configuration, and project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides staged user review, asset inventory, Wallpaper Engine testing, visible credits, and release-readiness validation.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
