## Description:

Countdown API connector for searching and reading eBay product and account data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Countdown API through the OOMOL `oo` CLI, including eBay autocomplete, product search, product details, and Countdown API account status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the OOMOL CLI by piping a remote script directly into a shell can execute installer code before review.

Mitigation: Use an official trusted OOMOL CLI source and inspect the installer or use a verified release path before installation.

## Reference(s):

- [Countdown API homepage](https://countdownapi.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-countdown-api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses include Countdown API data and OOMOL connector execution metadata when actions are run.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
