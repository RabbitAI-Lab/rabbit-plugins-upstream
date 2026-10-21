## Description:

Helps agents select and generate frontend color palettes, themes, and design tokens, then inspect contrast and color-vision distinctions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use it to select or generate color systems and assess them for frontend interfaces, charts, and visual assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Accessibility PASS reports and preview badges may be unreliable, so an inaccessible palette may appear validated.

Mitigation: Independently verify contrast and accessibility on finished pages; treat PASS reports and badges as advisory.

Risk: Preference and reference-file updates may persist and affect future runs or local content.

Mitigation: Review proposed changes and decide whether persistent updates are appropriate before accepting them.

Risk: An unreviewed installation may not match the release that was assessed.

Mitigation: Prefer reviewed, pinned installation versions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/aesthete-agent)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Design guidance and reports; palette and token data as JSON or CSS; HTML previews; shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operates offline; optional image-color extraction requires Pillow.]

## Skill Version(s):

0.10.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
