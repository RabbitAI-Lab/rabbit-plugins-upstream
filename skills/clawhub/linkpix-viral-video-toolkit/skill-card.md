## Description:

LinkPix helps agents analyze short-video links, derive reusable scripts, generate adapted marketing videos with qhkit, and extract audio from returned video URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, sellers, and marketing teams use this skill to turn Douyin/TikTok-style video links into adapted scripts, qhkit video generation commands, and audio extraction workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade executable tooling and change the user environment.

Mitigation: Use a pinned, reviewed local qhkit installation and review global npm, PATH, and shell-profile changes before allowing them.

Risk: The workflow requires qhkit or LinkPix to receive supplied video links, media, and generation prompts.

Mitigation: Use only media and links that are appropriate to share with the service, and avoid submitting sensitive or confidential material.

Risk: API tokens can be exposed if pasted into visible commands, logs, or shell history.

Mitigation: Provide tokens through protected secret handling or environment variables rather than inline command text.

Risk: Generated replicas and extracted audio can raise rights or licensing issues for commercial use.

Mitigation: Adapt scripts to the user's own product and review rights for music, audio, and source media before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-viral-video-toolkit)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces qhkit command sequences, status polling guidance, generated media URLs, audio extraction commands, and credit estimates when applicable.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
