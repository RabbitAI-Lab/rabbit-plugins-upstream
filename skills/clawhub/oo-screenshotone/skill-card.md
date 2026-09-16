## Description:

ScreenshotOne guides agents to use the OOMOL oo CLI connector for checking ScreenshotOne account usage, listing device presets, and capturing screenshots from URLs, HTML, or Markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run ScreenshotOne connector actions through an OOMOL-connected account for usage checks, viewport preset discovery, and website or markup screenshot capture.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Screenshot, animated screenshot, and bulk screenshot actions use an OOMOL-connected ScreenshotOne account and may trigger external, billable capture operations.

Mitigation: Review the exact URL, HTML, Markdown, and JSON payload before running capture actions, and confirm account or billing impact when relevant.

Risk: The skill includes first-time installer commands that pipe remote scripts into a shell.

Mitigation: Avoid curl-to-bash and irm-to-iex installer commands unless the installer source has been independently trusted and verified.

Risk: Capture actions are treated like safe reads in the artifact even though they can initiate external rendering work.

Mitigation: Treat take_screenshot, take_animated_screenshot, and take_bulk_screenshots as externally effectful operations and confirm payloads before execution.

## Reference(s):

- [ClawHub ScreenshotOne skill page](https://clawhub.ai/oomol/skills/oo-screenshotone)
- [ScreenshotOne homepage](https://screenshotone.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions may return JSON responses and generated screenshot, video, or GIF artifacts.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
