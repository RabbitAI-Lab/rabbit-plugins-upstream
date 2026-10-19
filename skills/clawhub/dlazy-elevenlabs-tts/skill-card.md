## Description:

Helps agents generate multilingual speech for dubbing, audiobooks, and character dialogue with selectable voices and voice controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn text into spoken audio for dubbing, audiobooks, and character dialogue.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to dLazy cloud services.

Mitigation: Review input content and selected files before invoking the skill; avoid submitting sensitive material without authorization.

Risk: An external npm CLI is installed or run and a dLazy API key may be stored locally.

Mitigation: Review the pinned CLI package before use and protect or rotate the API key as needed.

Risk: The sample response labels generated output as image/png despite this being a speech-generation skill.

Mitigation: Check actual output type and media URL before consuming or sharing generated results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI reports generated media URLs or an asynchronous task ID; the bundled output example incorrectly depicts an image rather than audio.]

## Skill Version(s):

1.3.31 (source: server-resolved ClawHub release; bundled skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
