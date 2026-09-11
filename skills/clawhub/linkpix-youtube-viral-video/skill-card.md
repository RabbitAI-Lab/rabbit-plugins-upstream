## Description:

Helps brand growth teams, creators, and ad teams generate YouTube commerce videos through Qinghu AI and qhkit, including unboxing reviews, long-form explainers, brand TVCs, and product recommendation videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketing teams, creators, and agent users use this skill to plan, estimate, generate, poll, and deliver YouTube-oriented product videos with qhkit. It guides model selection, image upload handling, cost confirmation, API key configuration, and video task status checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the user to provide a Qinghu API key through chat.

Mitigation: Use a limited or revocable Qinghu API key and prefer a secure secret manager or QHKIT_TOKEN environment variable for long-lived credentials.

Risk: The skill may install or upgrade qhkit and supporting image tools in a mutable environment.

Mitigation: Review the skill before installation and run qhkit in a sandboxed or pinned local environment where possible.

Risk: Video generation commands can consume credits and submitted tasks cannot be cancelled.

Mitigation: Confirm model, duration, orientation, language, input media, and estimated credits with the user before running generate commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-youtube-viral-video)
- [ClawHub Publisher Profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, text]

**Output Format:** [Markdown with qhkit shell commands and JSON parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce video task IDs, status summaries, cost estimates, and final video URLs returned by qhkit.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
