## Description:

Turns a document, topic, or brief into a narrated explainer, courseware, or training video using the dLazy CLI and hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create narrated explainer videos, report broadcasts, courseware, or training videos from documents, topics, and briefs. It is suited for workflows that can send prompts and selected files to dLazy's third-party hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected files, and the API key are handled by the dLazy CLI and hosted service.

Mitigation: Install only if comfortable using dLazy's third-party CLI and service, and avoid attaching confidential documents unless they are intended for upload to dLazy.

Risk: Ambiguous user requests could trigger video creation or file upload unexpectedly.

Mitigation: Confirm ambiguous requests before invoking the skill or attaching local files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-explainer-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text, Markdown, Configuration]

**Output Format:** [Markdown guidance with CLI commands and streamed service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or continue project-scoped dLazy chat sessions and may upload attached local files through the dLazy CLI.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
