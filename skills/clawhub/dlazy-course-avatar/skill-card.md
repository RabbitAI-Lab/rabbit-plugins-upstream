## Description:

Knowledge-course / online-teaching avatar lecturer - 16 landscape base-portrait recipes plus the slide-first pipeline that keeps a 20-minute lesson under 3000 credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External course creators, trainers, and developers use this skill to plan and generate a slide-first digital lecturer workflow for paid courses, enterprise training, public lessons, and LMS content. It focuses on reusable lecturer portraits, segmented narration, dLazy CLI commands, and cost-aware assembly guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow relies on a third-party CLI package and dLazy network services.

Mitigation: Install only if the publisher and @dlazy/cli package are trusted, avoid running npm or the CLI as root, and prefer least-privileged execution.

Risk: The workflow can use DLAZY_API_KEY and local dLazy configuration.

Mitigation: Protect the API key, avoid committing configuration files, and rotate the key if exposure is suspected.

Risk: Course files, prompts, images, or audio may be uploaded to the dLazy service.

Mitigation: Do not upload sensitive course material unless the user is comfortable sending it to the third-party service.

Risk: Paid model calls can consume credits, especially when avatar-driving steps are repeated.

Mitigation: Use dry-run checks, segment limits, and the skill's cost guidance before running batch generation.

Risk: Education and avatar content can create compliance issues if it implies guaranteed outcomes, false credentials, or undisclosed AI generation.

Mitigation: Review course copy and visuals before publication, avoid unverified credentials or outcome claims, and follow platform AI-content disclosure requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-course-avatar)
- [dLazy homepage](https://dlazy.com)
- [Skill overview](artifact/SKILL.md)
- [Course production pipeline](artifact/pipeline.md)
- [Base portrait recipes](artifact/recipes.md)
- [Troubleshooting and compliance](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dLazy CLI commands, payload JSON examples, budget checks, and compliance reminders.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
