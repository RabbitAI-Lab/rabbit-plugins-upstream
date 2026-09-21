## Description:

Operate fal.ai through an OOMOL-connected account by discovering models, retrieving pricing, submitting queue jobs, tracking status, fetching results, cancelling queued work, and retrieving webhook verification keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with fal.ai from an agent session through OOMOL's connector, including model discovery, cost lookup, async queue submission, status streaming, result retrieval, webhook key lookup, and request cancellation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can run a remote oo CLI installer when the CLI is missing.

Mitigation: Review and verify the installer through OOMOL's documented install guide or a trusted signed/package-manager path before allowing installation.

Risk: Some fal.ai actions can submit jobs, stream queue work, or cancel queued requests.

Mitigation: Confirm the exact payload, target endpoint, expected cost, and cancellation target before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fal-ai)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [fal.ai homepage](https://fal.ai)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector actions that return JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.5 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
