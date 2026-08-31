## Description:

Guides an agent through creating an online-course avatar lecturer using reusable 16:9 base portraits, slide-first production, text-to-speech, avatar driving, and assembly guidance for paid-course, training, or knowledge-sharing videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External course creators, training teams, and developers use this skill to plan and run a cost-conscious digital lecturer workflow for paid courses, enterprise training, public lessons, and internal LMS videos. The skill emphasizes when to use avatar footage, when to use slides with narration, and how to keep lecturer identity and audio consistent across long courses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may send prompts, images, audio, and course files to dLazy services and consume paid credits.

Mitigation: Confirm trust in the dLazy CLI package before use, review inputs for sensitive content, store API keys carefully, and use dry-run checks where available before paid generation.

Risk: Long-course generation can waste paid credits when avatar images, prompt lengths, file ordering, or video dimensions are wrong.

Mitigation: Use UTF-8 JSON input files for Chinese prompts, verify model flags with help output, test base images before driving video, zero-pad batch filenames, and inspect media properties before assembly.

Risk: Education-course avatar content can create compliance concerns if scripts or visuals imply guaranteed outcomes, fake credentials, or undisclosed AI-generated lecturers.

Mitigation: Avoid outcome guarantees and fictional endorsements, inspect generated visuals for badges or certificates, and disclose AI-generated lecturer imagery according to platform and legal requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-course-avatar)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [dLazy credits settings](https://dlazy.com/dashboard/organization/settings?tab=credits)
- [Skill definition and reference map](artifact/SKILL.md)
- [Course production pipeline](artifact/pipeline.md)
- [Base portrait and course visual recipes](artifact/recipes.md)
- [Troubleshooting and education compliance notes](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON payload examples, tables, and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dLazy CLI commands, model-selection guidance, UTF-8 JSON input patterns, ffmpeg commands, and cost estimates.]

## Skill Version(s):

1.0.1 (source: server release; artifact frontmatter: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
