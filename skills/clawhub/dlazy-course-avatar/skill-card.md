## Description:

Knowledge-course / online-teaching avatar lecturer with 16 landscape base-portrait recipes and a slide-first pipeline for producing paid-course, training, and knowledge-sharing avatar videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Course creators, training teams, and developers use this skill to plan and generate digital lecturer assets, scripts, narration, avatar clips, slide visuals, and assembly commands for online courses, corporate training, or internal learning videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow relies on an external npm CLI, dLazy APIs, and optional API credentials.

Mitigation: Install only if the dLazy package and service are trusted, prefer npx or an isolated project-local install where practical, and use scoped revocable API keys.

Risk: Course materials and generated assets may be uploaded to external dLazy services.

Mitigation: Avoid uploading confidential documents unless dLazy privacy and retention terms fit the use case.

Risk: Incorrect dimensions, prompt lengths, audio durations, or batching can waste credits or produce unusable course assets.

Mitigation: Use dry runs, JSON input files for Chinese prompts, documented duration limits, and the provided troubleshooting checks before running paid generation steps.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-course-avatar)
- [dLazy Homepage](https://dlazy.com)
- [Complete Pipeline](artifact/pipeline.md)
- [Recipe Library](artifact/recipes.md)
- [Troubleshooting and Compliance](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes dLazy CLI workflows, prompt recipes, cost planning guidance, and troubleshooting checks.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
