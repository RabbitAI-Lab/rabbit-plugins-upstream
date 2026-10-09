## Description:

Helps sellers analyze short-form video links, adapt marketing scripts, generate similar videos, and extract audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and content creators use this skill to break down short-form video examples, adapt scripts for their own products, generate marketing videos, or extract audio from linked videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow installs and runs a third-party package and sends supplied links or media to its service.

Mitigation: Review or pin the qhkit package version in controlled environments and share only media and links you are comfortable sending to the service.

Risk: The service requires an API token, and optional shell startup changes can persist after the session.

Mitigation: Handle the token as a secret and avoid persistent PATH changes unless intended.

Risk: Replicating video content or commercially reusing extracted background music can infringe others' rights.

Mitigation: Adapt scripts to original products and check usage rights before reusing video or audio commercially.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-viral-video-toolkit)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with script text, media links, and optional audio-file delivery]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation may return a task ID before the finished media link; audio extraction can produce a local MP3 file.]

## Skill Version(s):

0.1.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
