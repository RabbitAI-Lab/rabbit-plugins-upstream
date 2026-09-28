## Description:

Searches the ElevenLabs voice library by keyword, source, and category to help select voices and preview them before TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to search ElevenLabs voices by keyword, source, or category and choose a voice for TTS using preview results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented output and options include generic media and asynchronous behavior that may not match voice search.

Mitigation: Confirm the command returns voice metadata and audio previews before relying on its results.

Risk: The CLI sends prompts to a hosted service and documentation describes uploading local media paths.

Mitigation: Avoid confidential prompts and sensitive local file paths; review the skill before installing or invoking it.

Risk: A persistent global CLI installation may be undesirable.

Mitigation: Use the documented pinned npx invocation if you prefer not to retain a global CLI.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI source (skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search guidance covers keywords, voice source, category, and preview selection; actual voice metadata and preview availability require confirmation.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
