## Description:

Search the ElevenLabs voice library by keyword, source, and category to find voices and preview samples before text-to-speech use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers search and filter ElevenLabs voices, listen to available previews, and choose a voice for text-to-speech projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external CLI package and sending requests to a hosted service.

Mitigation: Review the package before installation; use the on-demand npx option if a global install is not desired.

Risk: API credentials may be stored locally, and supplied local media paths may be uploaded.

Mitigation: Protect and rotate credentials as needed; only pass media paths you intend to upload.

Risk: The documented sample response is generic image-output boilerplate rather than a verified voice-search result.

Mitigation: Check the actual voice matches and preview links before using them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI source listed in skill metadata (not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Voice search results with preview links; CLI responses may be JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Filter by keyword, source, and category; check actual results before relying on previews.]

## Skill Version(s):

1.3.28 (source: ClawHub release; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
