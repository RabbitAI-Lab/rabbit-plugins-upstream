## Description:

Runs confirmed short-drama image, video, speech, and music production jobs and saves the results and run records to the project.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to preview and explicitly approve bounded media-generation jobs for short dramas, then save generated assets and run records in their projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confirmed prompts and reference media are sent to configured provider APIs.

Mitigation: Review the exact preview and referenced media before approving production; use only trusted HTTPS provider destinations.

Risk: Untrusted adapter commands or exposed credentials can compromise project data.

Mitigation: Keep adapter configuration outside the project, trust only vetted adapter commands, and never store secrets in jobs or project documents.

Risk: Retrying a submitted production job may incur additional charges.

Mitigation: Check for recoverable provider results before retrying and require a fresh explicit confirmation for each retry.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/short-drama-produce)
- [Adapter contract](references/adapter-contract.md)
- [Seedance adapter](references/providers/seedance.md)
- [GPT Image 2 adapter](references/providers/gpt-image-2.md)
- [MiniMax H3 video adapter](references/providers/minimax-h3-video.md)
- [MiniMax speech adapter](references/providers/minimax-speech.md)
- [MiniMax Music adapter](references/providers/minimax-music.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Media files]

**Output Format:** [Text previews and run summaries, JSON job and status records, and generated image, video, speech, or music files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit confirmation for each production attempt; saves results and run records to the project.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
