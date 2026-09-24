## Description:

Adaptive Design Preference Engine learns visual preference signals from user choices and feedback, then maintains concise preference profiles for UI, graphic, video, and print design work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, developers, and creative teams use this skill to learn recurring visual preferences from design interactions and apply those preferences across UI, graphic, video, and print design tasks. The artifact states that 3D modeling, animation production, direct design-tool control, and brand asset management are out of scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad file, API, command, and persistent profiling behavior can expose design preferences, project context, or credentials if unnecessary permissions are granted.

Mitigation: Install with minimal read/write scope, avoid exec, API keys, callback URLs, and broad filesystem access unless clearly required, and review stored preference archives before reuse.

Risk: Long-lived preference archives can become stale, conflict with new user direction, or retain sensitive brand and client details.

Mitigation: Provide regular review, edit, delete, and conflict-resolution steps before applying archived preferences to new design work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/design)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance and concise preference entries, with a JSON response shape documented by the artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preference archives are organized into Aesthetic, By Medium, Brands, and Never sections; the artifact describes a 50-entry archive threshold and conflict handling.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
