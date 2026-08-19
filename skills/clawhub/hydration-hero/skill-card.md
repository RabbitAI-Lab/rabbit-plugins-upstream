## Description:

Smart water intake tracking based on body weight, weather, and activity level, with personalized hydration targets, caffeine and alcohol adjustments, streak tracking, hourly drinking schedules, and hydration education.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and developers can use this command-line skill to calculate hydration targets, log water intake and adjustment factors, generate drinking schedules, and review progress reports. Its wellness guidance should be treated as general information rather than medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat personalized hydration targets and urine-color guidance as medical advice.

Mitigation: Use the targets as general wellness guidance and follow clinician advice for pregnancy, illness, fluid-affecting medication, kidney, heart, liver, electrolyte, or fluid-restriction concerns.

Risk: The tool stores hydration, weight, activity, caffeine, alcohol, and related wellness logs locally in ~/.hydration_hero.json.

Mitigation: Protect the local user account and data file, avoid shared-machine use without appropriate access controls, and delete the file when the local history should be reset.

## Reference(s):

- [Hydration Science](references/hydration-science.md)
- [Hydration Schedule Guide](references/schedule-guide.md)
- [Source repository](https://github.com/voronindenis5/hydration-hero)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/hydration-hero)
- [Publisher profile](https://clawhub.ai/user/voronindenis5)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and terminal-oriented text with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local CLI output may include hydration targets, schedules, progress summaries, streaks, and wellness reminders.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
