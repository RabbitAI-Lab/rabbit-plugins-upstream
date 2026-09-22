## Description:

Turns article, blog, text, or batch source material into a scripted, synthesized, and published podcast episode with shownotes, images, RSS metadata, resumable TTS caching, and metadata update workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haohuawu](https://clawhub.ai/user/haohuawu)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and agents use this skill to convert source articles or provided text into a two-host podcast episode, validate the script and notes, synthesize audio, publish assets, and maintain episode metadata. It is also used for safe reruns, timeline calibration, and RSS/feed updates after publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The source-fetching fallback can expose browser proxy credentials if followed literally.

Mitigation: Avoid the proxy-credential extraction workflow, do not paste proxy passwords into shell commands, and use safer browser-mediated fetching or user-approved alternatives.

Risk: Publishing requires cloud storage credentials and can update podcast state and RSS metadata.

Mitigation: Use narrowly scoped TOS credentials limited to the intended podcast bucket or prefix, review proposed changes before publishing, and rely on the bundled validation and metadata update scripts.

Risk: Article images may be copied into published shownotes and feeds.

Mitigation: Review images before publishing and confirm that notes reference intended stable TOS-hosted image URLs.

Risk: Runtime dependencies and service clients may change behavior if installed without a lockfile.

Mitigation: Run the scripts in a pinned or locked environment where practical, and review dependency versions before production use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haohuawu/skills/podcast)
- [Script Specification](artifact/references/script-spec.md)
- [Notes Specification](artifact/references/notes-spec.md)
- [Images Guide](artifact/references/images-guide.md)
- [Source Fetching Guide](artifact/references/source-fetching-guide.md)
- [Podcast Channel Config Schema](artifact/assets/config.schema.json)
- [Doubao Speech Console](https://console.volcengine.com/speech)
- [Mic Tap Source Sample](https://freesound.org/people/susychristiansen/sounds/149034/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown scripts and notes, JSON channel configuration, shell commands, MP3 audio files, image assets, and RSS/feed metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces script.md, notes.md, optional article.md and images, podcast MP3 output, timeline data, episode state, and feed updates; upload behavior depends on configured TOS credentials.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
