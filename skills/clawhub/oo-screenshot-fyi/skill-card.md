## Description:

screenshot.fyi lets an agent operate screenshot.fyi through OOMOL's oo CLI to capture website screenshots and return generated URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to have an agent capture website screenshots through a connected screenshot.fyi account while inspecting live action schemas before constructing requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports that screenshot creation is under-labeled as read-like.

Mitigation: Confirm the target URL and expected account impact with the user before running take_screenshot.

Risk: The security evidence reports unverified pipe-to-shell installer commands for the OOMOL CLI.

Mitigation: Avoid pipe-to-shell installation commands unless the OOMOL CLI installation source has been independently verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-screenshot-fyi)
- [screenshot.fyi homepage](https://www.screenshot.fyi)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The screenshot action returns generated URLs and execution metadata from the screenshot.fyi connector.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
