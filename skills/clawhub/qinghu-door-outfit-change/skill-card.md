## Description:

Guides an agent through using Qinghu AI's qhkit workflow to generate door-opening outfit-change videos from one model image, up to four clothing images, and optional audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, commerce teams, and agents use this skill to prepare and submit paid Qinghu AI outfit-change video jobs for womenswear marketing and styling content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload model, clothing, and audio assets to Qinghu and spend Qinghu credits.

Mitigation: Use it only with assets the user is authorized to process, run an estimate first, and require explicit user approval before submitting a paid generation job.

Risk: The skill asks for an API key and may store it locally for qhkit access.

Mitigation: Prefer environment variables or another secure secret mechanism, avoid pasting secrets into chat, and rotate any exposed key.

Risk: The skill may install Node/npm packages and helper image tools at runtime.

Mitigation: Review package sources and installation commands before execution, and run the workflow in an environment where runtime package installation is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-door-outfit-change)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Markdown, Guidance]

**Output Format:** [Markdown with qhkit commands, JSON parameter examples, and user-facing status or delivery text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local image and audio paths, public media URLs, Qinghu workflow IDs, job log IDs, credit estimates, and generated video URLs.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
