## Description:

Turns a few photos and the details of an occasion into an AI video on varg: a wedding or birthday invitation and save-the-date that unfolds (the names and date printed right), a Christmas, New Year, Diwali, Eid or Lunar New Year greeting, old family photos brought to life, a love story across the eras for an anniversary, and a calm memorial or tribute film. Asks what the occasion needs, makes the stills first (GPT Image 2.5 prints names and dates), animates them (Seedance 2.5, Kling 4, Wan 3), adds music and exports for WhatsApp, a party screen or a service. Use when someone asks for a video invitation, an e-invite, a save-the-date, a wedding invitation video for WhatsApp, a holiday or festival greeting video, an animated e-card or Christmas card, "bring old photos to life", an anniversary or love-story video, or a memorial, celebration-of-life, retirement or farewell tribute. Not for birthdays (use varg-birthday-video) or editing real wedding footage (varg-video-editing).

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

External users create personalized invitation, holiday greeting, old-photo, anniversary, memorial, and tribute videos from occasion details and photos, then share or play them in messaging apps, on social media, or at events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal photos and occasion details may be sent to external AI services without a clear privacy disclosure.

Mitigation: Explain the external processing before generation, get consent for photos and details, and use only material the user has permission to share.

Risk: The installer is unpinned, so the installed source may change between releases.

Mitigation: Review the install command and installed skill source; use a versioned release where available.

Risk: The security analysis is partial because one local reference was unavailable.

Mitigation: Treat the scan as incomplete and review the missing reference or rerun the scan when it is available.

## Reference(s):

- [VARG guide to birthday and occasion videos](https://varg.ai/how-to/make-birthday-and-occasion-videos)
- [VARG MCP server](https://mcp.varg.ai/mcp)
- [Invitations and save-the-dates](artifact/references/invitations.md)
- [Holiday and festival greetings](artifact/references/holidays.md)
- [Old photos and tribute videos](artifact/references/old-photos.md)
- [Visual styles](artifact/references/styles.md)

## Skill Output:

**Output Type(s):** [Video files, Images, Audio, Guidance, Shell commands]

**Output Format:** [MP4 video with music, plus Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video orientation can be 9:16 or 16:9; duration and resolution depend on the occasion and selected generation workflow.]

## Skill Version(s):

1.0.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
