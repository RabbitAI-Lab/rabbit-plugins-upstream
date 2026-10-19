## Description:

Selects a dLazy audio model to generate speech, dialogue, music, or sound effects from a prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose and run dLazy audio generation for narration, dialogue, music, and sound effects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic CLI instructions and non-audio examples may prompt commands outside the requested audio task.

Mitigation: Keep commands scoped to the requested audio model and confirm any non-audio operation first.

Risk: The CLI can send prompts and local files to dLazy's cloud service.

Mitigation: Review inputs and approve any command that uploads local files before running it.

Risk: Audio generation can consume paid credits, and installing a third-party CLI adds package exposure.

Mitigation: Confirm credit-spending commands, review the external package, prefer the pinned npx invocation unless persistent installation is needed, and revoke the API key when no longer used.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI source (skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with shell commands and generated audio links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy service returns hosted audio output links; use requires an API key and may spend credits.]

## Skill Version(s):

1.3.32 (source: ClawHub release; bundled skill frontmatter says 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
