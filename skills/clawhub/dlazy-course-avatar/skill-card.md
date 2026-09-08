## Description:

Knowledge-course / online-teaching avatar lecturer - 16 landscape base-portrait recipes plus the slide-first pipeline that keeps a 20-minute lesson under 3000 credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External course creators, training teams, and developers use this skill to plan and generate slide-first course-avatar video workflows for paid courses, public lessons, internal training, and LMS content. It focuses on reusable lecturer portraits, segmented narration, dLazy CLI commands, and cost-aware assembly guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on an external dLazy CLI and cloud API that may receive course documents, portraits, voices, and generated media.

Mitigation: Use the skill only when the publisher and service terms are acceptable, review privacy and retention terms, and avoid uploading proprietary or personal material without authorization.

Risk: Installing or running the npm/npx CLI and providing DLAZY_API_KEY creates local environment and credential exposure risk.

Mitigation: Use a project-local or isolated environment, provide DLAZY_API_KEY only when needed, and avoid storing secrets in shared scripts or logs.

Risk: Generated education or training content could include unsupported learning-outcome promises or invented credentials if not reviewed.

Mitigation: Review scripts, prompts, and final course copy for prohibited pass-rate, guaranteed-outcome, institutional-endorsement, or fabricated-qualification claims before publication.

Risk: Incorrect dimensions, duration limits, prompt encoding, or media ordering can waste generation credits or produce unusable course media.

Mitigation: Use JSON input files for Chinese prompts, run dry runs where available, confirm current CLI flags with model help, and inspect generated assets before batch processing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-course-avatar)
- [dLazy Homepage](https://dlazy.com)
- [Skill Guide](artifact/SKILL.md)
- [Pipeline Guide](artifact/pipeline.md)
- [Recipe Library](artifact/recipes.md)
- [Troubleshooting and Compliance](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with bash command examples and JSON payload snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dLazy CLI invocations, prompt recipes, batch-processing steps, ffmpeg or Remotion assembly checks, and configuration guidance.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter version is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
