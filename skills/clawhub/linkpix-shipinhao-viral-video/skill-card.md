## Description:

Helps agents prepare and submit WeChat Channels short commerce video generation jobs through qhkit/LinkPix, including model selection, credit estimates, media upload, task polling, and delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, operators, and commerce teams use this skill to generate product seeding, storytelling, knowledge-talk, and live-stream promotion videos for WeChat Channels and related private-traffic placements. Agents use it to inspect available qhkit video models, collect required media and parameters, estimate credits, submit approved generation jobs, poll status, and return finished video links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade Node/npm tooling and qhkit during normal use.

Mitigation: Review installation commands before execution, prefer pinned or preinstalled qhkit where practical, and avoid unpinned npx fallbacks when possible.

Risk: The skill handles a QHKIT API token and uploads selected media to the Qinghu service.

Mitigation: Configure tokens outside chat when possible, avoid sharing secrets in prompts, and confirm that uploaded media is appropriate for the external service.

Risk: Generation commands can consume credits and create tasks that cannot be cancelled.

Mitigation: Run estimates first and require explicit user confirmation of model, duration, media, orientation, language, and expected credit use before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-shipinhao-viral-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit commands, credit estimates, task IDs, status updates, and final video URLs.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
