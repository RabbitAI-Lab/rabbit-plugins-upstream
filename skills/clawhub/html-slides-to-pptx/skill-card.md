## Description:

Creates HTML slide decks through guided intake, validates them against a supported HTML/CSS subset, and converts them to PowerPoint PPTX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cqcmj74](https://clawhub.ai/user/cqcmj74)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and presentation authors use this skill to turn presentation requirements into a structured slides workspace, generate compliant HTML slides, preview and validate them, and convert them to PPTX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the skill's tooling can download npm and Playwright dependencies.

Mitigation: Install in a trusted environment and review the bundled package metadata before running installation commands.

Risk: Converting slide HTML that contains remote URLs may cause the local machine to request external or internal network resources.

Mitigation: Use trusted slide HTML, prefer local images and fonts, and inspect or block remote URLs before previewing or converting decks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cqcmj74/skills/html-slides-to-pptx)
- [SKILL.md](artifact/SKILL.md)
- [HTML Conversion Specification](artifact/reference/html-spec.md)
- [Design Principles](artifact/reference/design-principles.md)
- [Interview Guide](artifact/reference/interview-guide.md)
- [Feature Coverage](artifact/scripts/test/FEATURE-COVERAGE.md)
- [VoltAgent awesome-design-md](https://github.com/VoltAgent/awesome-design-md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Configuration, Shell commands, Files]

**Output Format:** [Markdown guidance with HTML, CSS, JSON, JavaScript command examples, and generated project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create slides/, preview images, validation output, and a PPTX file; requires local node and npm.]

## Skill Version(s):

2.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
