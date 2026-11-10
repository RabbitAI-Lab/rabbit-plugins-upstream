## Description:

Turn slides or documents into narrated slideshow videos with voiceover and transitions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and teams can turn presentations and documents into narrated explainer, report, courseware, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an account credential and uses a CLI package that the scanner did not assess; some authentication and project-listing steps were not clearly tied to slideshow creation.

Mitigation: Review and trust the @dlazy/cli package and the account being used before signing in or running the workflow.

Risk: Attached files are uploaded to the dLazy media service for use by the hosted agent.

Mitigation: Check attached files for sensitive content and send only material intended for processing by the service.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, Text]

**Output Format:** [Narrated slideshow video with voiceover and transitions, plus text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video content is produced from user prompts and may use attached documents or images.]

## Skill Version(s):

1.0.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
