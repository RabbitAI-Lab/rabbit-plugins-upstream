## Description:

ScreenshotOne helps agents capture website, HTML, and Markdown screenshots through an OOMOL-connected ScreenshotOne account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to check ScreenshotOne usage, list device presets, and request website, HTML, Markdown, animated, or bulk screenshots through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute network-fetched scripts directly.

Mitigation: Prefer official, versioned installation steps with checksum or signature verification, and avoid elevated shells unless clearly required.

Risk: Screenshot inputs are sent through OOMOL and ScreenshotOne services.

Mitigation: Install and use only when sharing the provided URLs, HTML, Markdown, or capture targets with OOMOL and ScreenshotOne is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-screenshotone)
- [ScreenshotOne homepage](https://screenshotone.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce screenshot image, GIF, or video files depending on the ScreenshotOne action.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
