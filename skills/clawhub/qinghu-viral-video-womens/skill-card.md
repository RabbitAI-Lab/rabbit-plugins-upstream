## Description:

Qinghu AI video workflow helper that guides an agent through using a reference video and a model reference image to generate a women's fashion short video with transferred character motion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to prepare and run a paid Qinghu AI women's fashion video imitation workflow from authorized reference media. It helps gather workflow options, estimate credits, submit only after user approval, poll status, and return generated video outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can spend Qinghu credits when a generation job is submitted.

Mitigation: Run an estimate first, present the expected credit cost and key parameters, and submit only after explicit user approval.

Risk: Reference videos, model images, or API keys may be unauthorized or inappropriate for the intended use.

Mitigation: Use only media and credentials the user is authorized to provide, especially for commercial video generation.

Risk: Broad trigger wording could route adjacent video requests to this paid women's fashion workflow.

Mitigation: Confirm that the requested task matches the women's fashion video imitation workflow before estimate or submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-womens)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated video URLs, Qinghu credit estimates, job status, and final credit consumption.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
