## Description:

Helps agents generate short videos with MiniMax H3 from text, frame transitions, or reference media through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos with text prompts, starting and ending frames, or reference images, videos, and audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media are sent to the hosted dLazy service.

Mitigation: Share only prompts and media approved for third-party processing.

Risk: Login may store a dLazy API key locally.

Mitigation: Protect the local account and rotate or revoke keys if exposed.

Risk: Running the skill installs or invokes an external npm CLI.

Mitigation: Review the pinned package before use; prefer on-demand npx if a persistent global installation is unwanted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI source (linked in skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and links to generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation requests can return a media URL or an asynchronous task ID; the CLI can save the resulting asset locally.]

## Skill Version(s):

1.2.20 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
