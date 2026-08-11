## Description:

Searches the ElevenLabs voice library by keyword, source, and category, returning playable previews so users can choose voices for TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to search for ElevenLabs voices through the dLazy CLI before choosing a voice for TTS work. It is useful when a workflow needs voice discovery by keyword, source, category, or result count.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search prompts and CLI inputs may be sent to the hosted dLazy service.

Mitigation: Only submit intended search text and parameters, and avoid sensitive or unnecessary data in prompts.

Risk: A persistent global CLI install may expand local supply-chain and credential-management exposure.

Mitigation: Use the pinned npx invocation when a temporary install is preferred, and rotate or revoke the dLazy API key if it may have been exposed.

Risk: The artifact documentation includes generic cloud-generation details that may not apply directly to voice search.

Mitigation: Review `dlazy elevenlabs-search -h` and use dry-run behavior where available before sending inputs to the service.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI Metadata Link](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [JSON responses with CLI command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include playable preview URLs and asynchronous task status fields; the CLI requires a dLazy API key.]

## Skill Version(s):

1.3.6 (source: evidence.release.version; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
