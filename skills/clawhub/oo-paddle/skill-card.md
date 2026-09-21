## Description:

Paddle helps agents read, create, update, and archive Paddle catalog and customer data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Paddle products, prices, and customers through OOMOL-connected Paddle actions while checking live connector schemas before building payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute code retrieved from OOMOL-hosted URLs.

Mitigation: Review installation steps before use and prefer installing the oo CLI through a verified release or package manager.

Risk: Write and destructive Paddle actions can modify customer, product, and price data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before write, archive, reactivation, or destructive actions.

## Reference(s):

- [ClawHub Paddle skill page](https://clawhub.ai/oomol/skills/oo-paddle)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Paddle homepage](https://www.paddle.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas to shape action payloads and returns oo CLI responses as JSON when commands are run with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
