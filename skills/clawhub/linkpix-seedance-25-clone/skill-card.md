## Description:

Helps short-video creators, MCN teams, and brand marketers use Qinghu AI through qhkit to analyze a popular video link, adapt its emotional rhythm and visual style to their own product, and generate a Seedance 2.5-style video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, agencies, and marketing teams use this skill to recreate the structure, pacing, and visual feel of successful social videos for their own products while generating new scripts and video outputs through Qinghu AI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed if users paste secrets directly into chat.

Mitigation: Use secure secret storage or environment variables when available, and avoid sharing raw API keys in chat transcripts.

Risk: The workflow can install persistent npm tooling or execute update commands returned by CLI output.

Mitigation: Review the exact install or upgrade command before execution and verify the package source before installing or updating qhkit.

Risk: Source media and product assets may be uploaded to Qinghu AI for processing.

Mitigation: Use the skill only with media the user is authorized to upload to the third-party service.

Risk: Video generation can consume credits and create tasks that are not cancelable after submission.

Mitigation: Run an estimate when supported and obtain explicit user confirmation on model, duration, assets, and expected credits before generating.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-seedance-25-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key console](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated script or video-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit command output summaries, task IDs, credit estimates, and generated media URLs when the workflow completes.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
