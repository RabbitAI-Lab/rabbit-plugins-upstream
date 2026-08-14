## Description:

This release is labeled as a social media content generator, but the included README and executable script describe generating standalone landing-page HTML from text descriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and developers can use the included landing-page builder to generate standalone HTML pages from CLI flags, JSON configuration, or stdin text after reviewing the release mismatch. The package should not be treated as a social media content skill unless the publisher corrects the manifest, README, examples, references, and script entrypoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release metadata and skill manifest describe social media content generation, while the included README and executable code implement landing-page generation.

Mitigation: Do not install or rely on it as a social media content skill until the publisher corrects the manifest, README, examples, references, and script entrypoint to describe one coherent capability.

Risk: The executable writes generated HTML to local output paths, which may be used in automated publishing workflows.

Mitigation: Review generated HTML, links, images, claims, and output paths before publication or automation.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/voronindenis5/skills/landing-page-builder-2)
- [Server-resolved GitHub source](https://github.com/voronindenis5/landing-page-builder)
- [Landing page section reference](references/sections.md)
- [Theme configuration reference](references/themes.md)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell commands, JSON configuration examples, and generated standalone HTML/CSS files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Python standard library code and writes local HTML output paths selected by the user or configuration.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
