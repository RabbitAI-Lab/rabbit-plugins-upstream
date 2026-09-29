## Description:

Helps create multi-shot animated shorts with consistent characters, from scripts and shot prompts through visuals, audio, subtitles, and final video rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to plan and produce multi-shot animated videos with recurring characters using dLazy's hosted storyboard workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, project context, and explicitly attached files are sent to dLazy's hosted service.

Mitigation: Share only content approved for the service and review files before attaching them.

Risk: The dLazy CLI stores an API key in local configuration.

Mitigation: Protect local credentials and rotate or revoke the key from the dLazy dashboard if needed.

Risk: Using the skill requires installing and running a third-party CLI.

Mitigation: Review the package and linked CLI source before installing.

## Reference(s):

- [ClawHub storyboard skill release](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)
- [dLazy CLI repository (linked in release metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance, Media links]

**Output Format:** [Streamed text with links to generated assets where available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based conversations can continue across turns; generated assets may include visuals, audio, and video.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
