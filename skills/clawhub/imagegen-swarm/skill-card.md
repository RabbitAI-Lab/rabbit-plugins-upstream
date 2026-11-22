## Description:

Indie devs, creators, sellers: pool AI image quotas into one batch that keeps going if one runs out. Use when the user asks to generate an image, draw, edit an image, use reference images, make a video, or do text-to-image or text-to-video. Also use when the request names Codex, Grok, Grok Imagine, Gemini, nano banana, Antigravity, Jimeng, Dreamina, Muse, Lovart, gpt-image, or a pay-per-image API. Jimeng and Grok can make video. An optional pay-per-image API line (OpenAI or Gemini API) runs when a job names api, or when no enabled subscription engine can take that job. Jimeng can edit from up to 10 reference images. Antigravity Gemini edits up to 3 reference images. The optional paid Gemini API allows 3 references for gemini-2.5-flash-image and 14 for later Gemini image models. For a shared character, brand, mascot, or cover series, ask before enabling series mode. Not for crop, resize, convert, or other ordinary local image processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ekko237](https://clawhub.ai/user/ekko237)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images and videos through supported AI services, including batching jobs across available engines. It can also prepare consistent image series and optionally use a user-configured pay-per-image service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan warns that some approval behavior may not reliably verify the complete requested operation, and some components were only partially inspected.

Mitigation: Review the approval behavior and remaining scripts before installation; consider avoiding installation until the approval behavior is clarified or corrected.

## Reference(s):

- [Codex engine details](artifact/references/codex.md)
- [Lovart engine details](artifact/references/lovart.md)
- [Muse approval scope](artifact/references/muse.md)

## Skill Output:

**Output Type(s):** [Images, Videos, JSON, Text]

**Output Format:** [Image and video files with JSON result summaries and text status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media can be saved as PNG or MP4; image series may include consistency scores.]

## Skill Version(s):

1.4.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
