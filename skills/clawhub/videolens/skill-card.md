## Description:

VideoLens turns user-selected YouTube videos, local files, or supported video URLs into timestamped reports grounded in transcript, frame-level vision, OCR, and OpenAI BYOK analysis after explicit install and credit approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shadoprizm](https://clawhub.ai/user/shadoprizm)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, QA teams, creators, and product teams use this skill to convert selected videos into grounded summaries, tutorials, meeting notes, bug reports, UX reviews, privacy reviews, and production recipes. It is intended for manual use where the user approves runtime installation separately from OpenAI API-credit spending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bootstrap downloads code and dependencies from GitHub and package registries.

Mitigation: Require explicit runtime-install approval and rely on the pinned, hash-verified runtime and locked dependency set described by the release evidence.

Risk: Analysis sends selected video audio, frames, transcripts, and prompts to OpenAI using the user's BYOK key.

Mitigation: Require separate API-credit approval before analysis, use a dedicated OpenAI key or limited budget where practical, and avoid analyzing content the user is not authorized to process.

Risk: Generated reports and caches may retain sensitive video-derived content locally.

Mitigation: Store artifacts only in the managed VideoLens state directory and remove reports or caches when they are no longer needed.

Risk: Privacy, UX, bug, or content findings may be incomplete or mistaken.

Mitigation: Treat generated findings as review aids and verify consequential claims against the cited timestamps.

## Reference(s):

- [VideoLens ClawHub listing](https://clawhub.ai/shadoprizm/skills/videolens)
- [VideoLens product site](https://videolens.io)
- [VideoLens Chrome extension](https://videolens.io/chrome)
- [VideoLens GitHub repository](https://github.com/shadoprizm/videolens)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown report, HTML report, JSON analysis, file paths, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are stored as local run artifacts; analysis can reuse cached extraction when source and settings match.]

## Skill Version(s):

1.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
