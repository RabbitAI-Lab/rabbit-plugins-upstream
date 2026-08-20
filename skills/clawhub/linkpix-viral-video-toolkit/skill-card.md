## Description:

LinkPix helps agents use the qhkit CLI to analyze short-video links, derive viral video scripts, recreate adapted marketing videos, and extract audio from source videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, sellers, and agents use this skill to turn Douyin, TikTok, or similar video links into adapted scripts, generated marketing videos, or extracted audio/BGM. It is most useful when a user asks to analyze, recreate, or extract media from a reference short video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade global qhkit tooling on the local machine.

Mitigation: Review before installing on shared, production, or sensitive machines and prefer a project-local or isolated qhkit install where practical.

Risk: The skill can reuse stored account credentials or prompt users to configure an API token.

Mitigation: Confirm which account token will be used and avoid placing API tokens directly in shell commands.

Risk: Video generation tasks can spend service credits and may run for an extended time.

Mitigation: Use estimate commands before generation, confirm credit sufficiency, and report task IDs plus expected wait times.

Risk: Recreating videos or extracting BGM can raise content-rights concerns.

Mitigation: Adapt scripts to the user's product and review BGM or source-media rights before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-viral-video-toolkit)
- [Publisher profile: autoagc](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iqinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated media URLs, task IDs, credit estimates, and CLI status messages.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
