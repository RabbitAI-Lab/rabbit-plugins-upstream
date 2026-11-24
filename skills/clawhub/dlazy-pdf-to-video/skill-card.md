## Description:

Turns user-provided PDFs into explainer, report, courseware, or training videos through parsing, outlining, storyboarding, voiceover, building, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams can use this skill to turn a PDF into an explainer, report broadcast, courseware, or training video by working with dLazy's file-to-video service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the hosted service sends prompts to dLazy, and attached local files are uploaded to its media storage.

Mitigation: Use the service only for documents permitted by your organization's data-handling rules; avoid attaching sensitive files unless approved.

Risk: The security verdict has medium confidence, and the CLI login, project listing, and external CLI package were not fully assessed.

Mitigation: Before installing, review the skill's install instructions and the pinned CLI package, and consider whether login and project listing are needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Video, Text, Shell commands, Guidance]

**Output Format:** [Generated explainer video with CLI conversation text and guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped workflow; requires a dLazy API key. Attached local files are uploaded to dLazy media storage.]

## Skill Version(s):

1.0.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
