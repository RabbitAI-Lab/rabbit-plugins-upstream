## Description:

Guides agents through building online-course avatar lecturer videos with 16 landscape base-portrait recipes and a slide-first pipeline for paid courses, training modules, knowledge-sharing videos, and internal LMS content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External course creators, training teams, and developers use this skill to plan, script, generate, and assemble AI avatar lecturer videos for paid courses, public lessons, enterprise training, and internal LMS modules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses paid dLazy cloud video tools and may upload course materials to dLazy services.

Mitigation: Install and run it only when that cloud processing and paid credit usage are acceptable for the course materials.

Risk: Authentication can store a dLazy API key in ~/.dlazy/config.json or use DLAZY_API_KEY.

Mitigation: Protect the credential, avoid committing local config files, and rotate or revoke the key if it is exposed.

Risk: The source instructions are primarily Chinese and include cost, authentication, and compliance details.

Mitigation: Non-Chinese readers should translate and review those sections before running commands.

Risk: AI-generated lecturer videos for education can create disclosure, claims, and qualification risks.

Mitigation: Review course copy and generated visuals for AI-content disclosure, unsupported outcome promises, and invented credentials before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-course-avatar)
- [dLazy homepage](https://dlazy.com)
- [Pipeline guide](artifact/pipeline.md)
- [Recipe library](artifact/recipes.md)
- [Troubleshooting and compliance guide](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes cost estimates, model parameter guidance, and execution cautions for paid dLazy cloud APIs.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
