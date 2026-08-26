## Description:

Converts PPT, Word, Excel, PDF, and other documents into videos by using dLazy to parse content, outline the narrative, create storyboards, add voiceover, build the video, and validate the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill when they have a document and want an explainer video, report broadcast, courseware, or training video. It helps an agent invoke the pinned dLazy file-to-video workflow, continue project conversations, and handle authentication or service errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, options, and selected documents to dLazy API and file storage endpoints.

Mitigation: Use it only with content approved for dLazy processing, and avoid attaching sensitive or regulated files unless the user's organization has approved the service terms.

Risk: The security evidence says the API-key storage claim is stronger than what the pinned CLI actually enforces.

Mitigation: Prefer passing DLAZY_API_KEY per run or manually restrict permissions on ~/.dlazy/config.json after login; rotate or revoke the key from the dLazy dashboard if exposure is possible.

Risk: The workflow depends on external dLazy service availability, authentication state, and organization credits.

Mitigation: Confirm authentication and available credits before relying on the skill for time-sensitive work, and surface unauthorized or insufficient-balance errors directly to the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy CLI metadata source link](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and streamed CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow may upload user-selected local files to dLazy storage and return project-scoped responses from the hosted dLazy agent.]

## Skill Version(s):

1.3.8 (source: ClawHub release metadata; artifact frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
