## Description:

Search the ElevenLabs voice library by keyword, source, and category, and return playable previews to help select a voice for text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators can search ElevenLabs voices by a short descriptor, source, and category, then review playable previews before choosing a voice for text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches use the third-party dLazy service and may consume account credits.

Mitigation: Review dLazy privacy terms and the pinned CLI package before use; run --dry-run to inspect request details and estimated cost.

Risk: The CLI requires a dLazy API credential.

Mitigation: Prefer device-code login or environment authentication over pasting API keys into chat; rotate or revoke keys through the dLazy dashboard when needed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or text listing matching voices, search details, and playable preview links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results vary with search terms, selected filters, and account access; the service requires dLazy authentication.]

## Skill Version(s):

1.3.35 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
