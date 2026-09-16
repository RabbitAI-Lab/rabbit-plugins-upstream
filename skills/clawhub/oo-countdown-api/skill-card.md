## Description:

Provides OOMOL-connected access to Countdown API for searching eBay products, reading product details, retrieving autocomplete suggestions, and checking account usage or platform status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run read-oriented Countdown API actions through an OOMOL-connected account without handling raw API tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include one-line remote installer commands that can execute arbitrary code if the installer delivery path is not trusted.

Mitigation: Review the skill before installing, avoid running remote installer commands unless OOMOL's installer source is trusted, and prefer a verified, versioned, or package-manager installation method when available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-countdown-api)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Countdown API homepage](https://countdownapi.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented Countdown API actions through the OOMOL oo CLI; setup guidance is used only after authentication or connection failures.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
