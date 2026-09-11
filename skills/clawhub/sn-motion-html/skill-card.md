## Description:

Build continuous-shot, motion-driven HTML stories from a subject or narrative with research, story structure, AI stills, Seedance clips, interface styling, media normalization, and browser QA.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative producers use this skill to plan and build scene-based, continuous-camera web stories that combine source research, generated stills, Seedance video clips, and responsive HTML playback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials and local project content may be sent to an unvalidated Ark endpoint.

Mitigation: Use only a trusted project-local .env file, verify the Ark base URL before generation, and avoid running the pipeline on untrusted project folders.

Risk: Manifest-controlled paths may allow absolute paths or parent-directory traversal.

Mitigation: Inspect video-manifest.json for absolute paths or ../ traversal before generation and keep project inputs confined to trusted directories.

Risk: A static preview server can expose secrets if hidden files are served.

Mitigation: Use the provided local preview server or another host configuration that denies .env and other hidden files.

## Reference(s):

- [Production workflow](references/workflow.md)
- [Project schemas](references/schemas.md)
- [Prompting patterns](references/prompting.md)
- [Style presets](references/style-presets.md)
- [Seedance integration](references/seedance.md)
- [Motion frontend](references/frontend.md)
- [Volcengine Seedance API documentation](https://www.volcengine.com/docs/82379/1520757?lang=zh)
- [Volcengine Seedance task documentation](https://www.volcengine.com/docs/82379/1521309?lang=zh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON manifests, shell commands, Python scripts, and HTML/CSS/JavaScript project files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API requests to a configured Ark/Seedance endpoint and local media files after explicit authorization.]

## Skill Version(s):

2026.9.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
