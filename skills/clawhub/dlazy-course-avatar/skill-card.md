## Description:

Knowledge-course and online-teaching avatar lecturer guidance with 16 landscape base-portrait recipes and a slide-first pipeline for creating paid-course, training, or knowledge-sharing videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, educators, and training teams use this skill to plan and generate digital-human course videos from scripts, slides, documents, and reusable lecturer assets. It helps agents produce cost-aware dLazy CLI workflows, prompt recipes, payload guidance, and publishing checks for paid courses, corporate training, and LMS content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can spend paid dLazy credits through CLI/API calls.

Mitigation: Use dry-run or equivalent review steps before execution and confirm budget-sensitive commands before running paid generation.

Risk: The workflow may require storing or passing a dLazy API key and uploading course materials, audio, images, and generated video assets to provider services.

Mitigation: Install only when that data handling is acceptable, use the documented dLazy authentication paths, and avoid uploading sensitive course materials without approval.

Risk: Generated course-avatar content can create education-advertising or platform-compliance issues if it implies guaranteed outcomes, fabricated credentials, or undisclosed AI-generated lecturers.

Mitigation: Review generated scripts, visuals, and final videos for platform rules and education-ad compliance before publishing.

## Reference(s):

- [Skill Overview](artifact/SKILL.md)
- [Course Avatar Pipeline](artifact/pipeline.md)
- [Portrait and Slide Recipes](artifact/recipes.md)
- [Troubleshooting and Compliance Notes](artifact/troubleshooting.md)
- [dLazy Homepage](https://dlazy.com)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-course-avatar)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose dLazy CLI calls, local file paths, JSON payloads, cost estimates, and media-production review steps.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
