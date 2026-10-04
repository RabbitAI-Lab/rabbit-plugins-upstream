## Description:

Analyzes short-video links with LinkPix/qhkit to derive viral-video scripts, recreate adapted marketing videos from those scripts and product images, or extract audio from the discovered video URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, sellers, and marketing operators use this skill to analyze Douyin/TikTok-style video links, adapt the resulting script to their own products, generate similar marketing videos, or extract audio for review and reuse where permitted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running upgrade commands copied from a CLI response can create unsafe local command-execution exposure.

Mitigation: Use only a fixed, reviewed qhkit upgrade command, and run it only after explicit user approval.

Risk: The workflow sends video links, uploaded local media paths, and an API token through qhkit and external LinkPix services.

Mitigation: Install qhkit only from trusted registries, protect QHKIT_TOKEN, and avoid using sensitive or confidential media with this workflow unless the service is approved.

Risk: Recreating videos or extracting BGM may create copyright or licensing issues for commercial reuse.

Mitigation: Adapt scripts and visuals to the user's own product and verify rights for source videos, audio, and generated outputs before commercial publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-viral-video-toolkit)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown]

**Output Format:** [Markdown with inline bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, generated media URLs, credit estimates, polling guidance, and CLI error messages.]

## Skill Version(s):

0.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
