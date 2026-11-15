## Description:

Turn an article, notes, or a finished script into a listener-ready solo podcast episode with a consistent host voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Podcast creators and producers use this skill to adapt supplied material into an episode script and narrated audio, with recurring host direction, optional dialogue, and audio finishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports broad permissions, persistent credentials shared across packages, and automatic installation and runtime reporting; inspection was partial.

Mitigation: Review the reported permissions and reporting behavior before installation, and inspect the remaining components and unresolved references before relying on the skill.

Risk: Credentials may persist across packages, increasing exposure if a local installation or another package is compromised.

Mitigation: Use a dedicated Beatra account where practical, keep credential files restricted to the local user, and disconnect or remove credentials when they are no longer needed.

## Reference(s):

- [Beatra skill homepage](https://beatra.ai/skills/ai-podcast-voiceover)
- [ClawHub release page](https://clawhub.ai/beatra-ai/skills/ai-podcast-voiceover)
- [Episode script guidance](references/episode-script.md)
- [Show profile](references/show-profile.md)
- [Speech, voices, cloning, and audio finishing](references/speech-and-audio.md)
- [Updates and security](references/updates-and-security.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, MP3 audio, Subtitles]

**Output Format:** [Episode scripts and production notes in Markdown; synthesized audio as MP3, with aligned subtitles when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long episodes and dialogue may be delivered in chunks; optional music, sound effects, and audio finishing are separate outputs.]

## Skill Version(s):

0.2.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
