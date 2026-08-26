## Description:

Turns scripts, screenplays, or shot lists into storyboarded video projects with scene breakdowns, shot generation, assembly, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and production teams use this skill to ask an agent to create or continue dLazy storyboard projects from scripts, scene breakdowns, reference files, and follow-up prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to dLazy hosted services.

Mitigation: Attach only files intended for the project and use the skill only where dLazy hosted processing is acceptable.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Use per-run DLAZY_API_KEY when persistence is not desired, and rotate or revoke organization keys when access should end.

Risk: The skill invokes a pinned npm CLI that communicates with dLazy API and file-storage endpoints.

Mitigation: Review the pinned CLI package and source before installation in controlled environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and streamed agent responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project ids, authentication status, uploaded file handling, storyboard progress, and hosted-service errors.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
