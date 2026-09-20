## Description:

ScreenshotOne lets agents operate ScreenshotOne through an OOMOL-connected account to inspect schemas, capture website, HTML, or Markdown screenshots, submit bulk captures, and query usage or device presets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run ScreenshotOne capture and account-inspection actions through OOMOL's connector without handling raw ScreenshotOne credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance may ask the agent to install the oo CLI by running an internet-hosted installer script.

Mitigation: Verify the oo CLI through OOMOL's official installation process before running installer commands.

Risk: Screenshot, animated, and bulk capture requests may transmit supplied URLs, HTML, Markdown, or page content and may consume ScreenshotOne or OOMOL account credits.

Mitigation: Confirm capture payloads and expected account-credit impact with the user before submitting write or bulk actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-screenshotone)
- [ScreenshotOne homepage](https://screenshotone.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce ScreenshotOne image, video, or GIF capture files through the connector.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
