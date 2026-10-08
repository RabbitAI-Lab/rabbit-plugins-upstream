## Description:

Search the ElevenLabs voice library by keyword, source, and category to find voices and playable previews for TTS selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users search available ElevenLabs voices by description, source, or category and inspect previews before choosing a voice for TTS.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search prompts and parameters are sent to the third-party dLazy cloud service.

Mitigation: Avoid submitting sensitive prompts or parameters; review the service terms before use.

Risk: Authentication may save a dLazy API key locally, and using the skill can install a third-party npm package.

Mitigation: Review the pinned CLI package before installation and protect or rotate the locally stored API key.

Risk: The documented output example appears inconsistent with voice-search results.

Mitigation: Check actual CLI output before relying on documented fields or preview links.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with shell commands and voice-search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice matches may include playable preview links; the documented example response shape may be inaccurate.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
