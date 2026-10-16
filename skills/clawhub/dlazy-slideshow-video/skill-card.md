## Description:

Turns slides and documents into narrated slideshow videos with voiceover and transitions through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and teams can turn presentations, reports, and other documents into narrated explainer or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents may be sent to dLazy's hosted service.

Mitigation: Share files only when this data flow is acceptable; avoid sensitive documents otherwise.

Risk: Authentication saves an API key in the local CLI configuration.

Mitigation: Protect local credentials and rotate or revoke the key if exposed.

Risk: Using the external CLI installs or runs third-party software.

Mitigation: Review the CLI/package before use and prefer the pinned npx invocation if a global install is undesirable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text responses and command-line guidance for narrated slideshow video projects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video creation uses dLazy's hosted service and requires an API key.]

## Skill Version(s):

1.0.27 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
