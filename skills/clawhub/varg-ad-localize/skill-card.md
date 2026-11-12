## Description:

Turns one video ad into versions for 8+ TikTok Shop and Meta markets on varg: transcreates the script per market (hook, slang, claims, units, local price and currency from an offer card, each line fitted to its time slot), voices it with ElevenLabs v4 in the same voice, lip-syncs only shots where a face talks for more than 1.5 s (Sync v3), rebuilds captions and on-screen text in the target language instead of inpainting them, re-cuts every shot on the new language's words, and ends with a native-review checklist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT

## Use Case:

Sellers and marketing teams use this skill to create localized versions of short video ads for different TikTok Shop and Meta markets. It transcreates the script, produces a matching voice track, rebuilds captions and on-screen text, and provides a checklist for native review before launch.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installation example uses an unpinned package, which can change between installs.

Mitigation: Review the installer before use and prefer a reviewed, version-pinned installer where available.

Risk: Scripts, media, voice, and facial footage may be sent to external services during localization.

Mitigation: Confirm consent and data-handling expectations before sending source material to varg and the named voice or lip-sync services.

Risk: The security scan was partial because several local references could not be resolved, so its evidence is incomplete.

Mitigation: Review the unresolved references and the current installation and service requirements before use.

## Reference(s):

- [varg how-to guides](https://varg.ai/how-to)
- [varg MCP connection](https://mcp.varg.ai/mcp)
- [Sync lip-sync quality guidance](https://sync.so/docs/compatibility-and-tips/improving-lip-sync-quality)
- [ClawHub skill release](https://clawhub.ai/vargai/skills/varg-ad-localize)

## Skill Output:

**Output Type(s):** [Video files, Text, Guidance]

**Output Format:** [Localized MP4 video with a native-review checklist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one dubbed and re-captioned video per target market; the checklist calls for native review of wording, prices, claims, calls to action, and AI labeling.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
