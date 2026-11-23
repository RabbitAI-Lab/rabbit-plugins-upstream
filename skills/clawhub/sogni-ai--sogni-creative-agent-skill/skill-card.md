## Description:

An agent skill for generating and editing images, video, music, speech, and 3D assets through Sogni AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sogni-ai](https://clawhub.ai/user/sogni-ai)

### License/Terms of Use:

MIT

## Use Case:

Creators and agent users use the skill to generate or transform visual, video, and audio media, manage reusable creative references, and retrieve results through Sogni. It can also guide agents through connected workflows such as video editing and playable world creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private photos, voices, or identity references may be processed remotely, and privacy guidance may not fully describe that handling.

Mitigation: Avoid submitting sensitive personal media unless you are comfortable with the service's processing; review applicable privacy terms first.

Risk: The security review reports instructions that may work around model safety refusals.

Mitigation: Keep the host model's safety boundaries in place and do not use the skill to bypass a refusal.

Risk: The security review flags installation and security concerns and says its analysis is partial.

Mitigation: Review the package and its installation requirements before installing, and treat the scanner's review as incomplete.

## Reference(s):

- [Sogni AI](https://sogni.ai)
- [Sogni Creative Agent Skill on ClawHub](https://clawhub.ai/sogni-ai/skills/sogni-creative-agent-skill)
- [Sogni Creative Agent Skill on npm](https://www.npmjs.com/package/@sogni-ai/sogni-creative-agent-skill)
- [Sogni API key setup](https://dashboard.sogni.ai/api-key)
- [Image prompting guide](references/image-prompting.md)
- [Video prompting guide](references/video-prompting.md)
- [Hosted API guide](references/hosted-api.md)

## Skill Output:

**Output Type(s):** [Image files, Video files, Audio files, 3D model files, Segmentation masks, Structured text and JSON]

**Output Format:** [Generated media files with text or JSON metadata and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media type, model, resolution, and other generation settings depend on the requested task.]

## Skill Version(s):

3.73.2 (source: frontmatter, changelog, released 2026-11-22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
