## Description:

LinkPix helps agents analyze viral short-video links, extract scripts or audio, and generate adapted marketing video remakes through the qhkit CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketplace sellers, and agents use this skill to analyze Douyin/TikTok-style video links, derive remake scripts, generate adapted marketing videos from user product images, or extract audio from returned video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party qhkit CLI may receive video links, uploaded media, and API-token-backed requests.

Mitigation: Use the CLI only when the user is comfortable sending that data to the service, and avoid submitting sensitive or unapproved media.

Risk: Video generation can consume service credits.

Mitigation: Run an estimate when supported and obtain explicit user confirmation before creating generation tasks.

Risk: Generated remakes or extracted audio could copy protected scripts, footage, or music.

Mitigation: Adapt scripts to the user's own product and use rights-cleared assets and audio for commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-viral-video-toolkit)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents through qhkit task submission and polling that return JSON status, video URLs, audio files, and credit usage after user confirmation.]

## Skill Version(s):

0.1.1 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
