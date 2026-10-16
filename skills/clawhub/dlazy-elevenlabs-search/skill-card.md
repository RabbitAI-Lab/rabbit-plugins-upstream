## Description:

Helps agents search the ElevenLabs voice library by keyword, source, and category and select a voice for text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and content creators use this skill to find voices by description, source, or category before choosing one for text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party CLI requires a dLazy API key and sends searches to dLazy-hosted services.

Mitigation: Review the CLI before installation, protect the key, and send only data approved for the service.

Risk: The documentation describes local uploads, generation, and image results that do not clearly match voice search.

Mitigation: Avoid passing local files and verify the actual output and file-handling scope with the publisher before relying on the skill.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown instructions with CLI examples; the CLI reports JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice previews are claimed, but the documented sample instead shows an image result.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
