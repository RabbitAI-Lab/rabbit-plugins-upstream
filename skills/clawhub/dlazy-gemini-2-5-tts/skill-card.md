## Description:

Generates multilingual, natural-sounding speech from text using Gemini 2.5 TTS through the dLazy CLI and hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to turn text prompts into Chinese or English speech, select supported voices, and retrieve generated audio outputs through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local API-key storage security may be overstated.

Mitigation: Prefer passing DLAZY_API_KEY per invocation or manually restrict permissions on ~/.dlazy/config.json after login.

Risk: Prompts are sent to dLazy and generated outputs are hosted by dLazy.

Mitigation: Review data sensitivity and service terms before sending prompts or relying on hosted output URLs.

Risk: A global CLI installation persists executable code on the system.

Mitigation: Use the pinned npx invocation when a persistent global install is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses containing generated audio URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; generated output URLs are hosted by dLazy.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter says 1.3.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
