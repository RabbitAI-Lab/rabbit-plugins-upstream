## Description:

HyperFrames routes video, animation, motion-graphic, slideshow, Remotion-port, and existing-project requests into the appropriate HyperFrames workflow, using supplied URLs, PRs, Figma designs, briefs, footage, or music as inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and agent operators use this skill as the entry point for HyperFrames video work. It resumes existing projects, clarifies fresh requests, selects the owning workflow, and guides editing, validation, rendering, or publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run HyperFrames npm/npx tooling and update workflow skills.

Mitigation: Install and run it only in projects where those commands are expected, and review command output before relying on generated or modified project artifacts.

Risk: Video workflows may read supplied URLs, media, GitHub PRs, Figma inputs, credentials, and publish targets.

Mitigation: Use project-scoped inputs, avoid unnecessary sensitive material, and review allowed URLs, credentials, and publish commands for sensitive projects.

Risk: Website capture and publishing can expose content or create public links when requested.

Mitigation: Confirm capture scope and publishing intent before running those workflow steps, especially for private or unreleased material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes)
- [Capability menu](references/capability-menu.md)
- [Intent interview](references/intent-interview.md)
- [Skill lifecycle](references/skill-lifecycle.md)
- [Workflow route contracts](references/routes/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and project-file instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May route to workflow skills that create or update HyperFrames project files, render media, capture websites, or publish outputs when requested.]

## Skill Version(s):

1.0.23 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
