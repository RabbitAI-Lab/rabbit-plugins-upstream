## Description:

Turns PPT, Word, Excel, PDF, and other documents into explainer, report, courseware, or training videos through parsing, outlining, storyboarding, voiceover, synthesis, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People creating explainers, report walkthroughs, courseware, or training videos can use this skill to turn office documents and PDFs into a narrated video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags report-interpretation triggers as broader than the stated document-to-video purpose.

Mitigation: Check that report interpretation is intended for the task before invoking the skill.

Risk: Prompts and attached files are sent to dLazy for processing, and the security guidance asks reviewers to examine the login and organization project-listing actions.

Mitigation: Review prompts and files before sending them, avoid sharing material that should remain private, and confirm login and project listing are appropriate for the task.

Risk: The security evidence says some references could not be resolved, so its review is incomplete.

Mitigation: Review the skill and its linked material before installing or using it.

## Reference(s):

- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, Configuration instructions, Video files]

**Output Format:** [Conversational text and CLI commands; video deliverables are produced through the dLazy service.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped sessions can continue across turns; attached files are sent to the service for processing.]

## Skill Version(s):

1.3.44 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
