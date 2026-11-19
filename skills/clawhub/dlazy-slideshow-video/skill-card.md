## Description:

Turn slides or documents into narrated slideshow videos with voiceover and transitions when a slideshow-style video is requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can turn presentations and documents into narrated explainer, report, courseware, or training videos through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious because scanners report organization project-listing and login actions that do not clearly match its slideshow-video purpose, as well as a broad activation trigger; the verdict does not establish malicious intent.

Mitigation: Review the dLazy CLI's authentication and project-listing behavior and confirm the activation scope before use.

Risk: Prompts and attached files are sent to dLazy's hosted API and media storage.

Mitigation: Only send documents and credentials that are approved for use with the hosted service.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Video files, Text]

**Output Format:** [Generated slideshow video with text responses in the CLI; video encoding depends on the hosted service.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Attached local files are uploaded to dLazy storage before processing.]

## Skill Version(s):

1.0.39 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
