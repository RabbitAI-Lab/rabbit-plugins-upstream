## Description:

Operates the Screenshotbase connector through the OOMOL-connected oo CLI to check quota usage and capture webpages as hosted screenshot URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run Screenshotbase actions from an agent, including quota checks and webpage screenshot capture through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes pipe-to-shell installation commands for the oo CLI.

Mitigation: Install the oo CLI through a verified, pinned, or signed method before using the skill.

Risk: The take_screenshot action sends target webpage data to an external Screenshotbase capture service.

Mitigation: Use it only for URLs intended for Screenshotbase processing, and avoid sensitive, authenticated, private, or internal pages unless explicitly authorized.

Risk: The screenshot action is described as a read-style action even though it creates an external capture artifact.

Mitigation: Review the target URL and expected capture result before running screenshots in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-screenshotbase)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Screenshotbase homepage](https://screenshotbase.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return JSON responses from oo connector actions, including quota data, execution IDs, and hosted screenshot URLs.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
