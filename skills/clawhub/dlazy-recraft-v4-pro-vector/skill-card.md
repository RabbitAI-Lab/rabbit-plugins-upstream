## Description:

High-fidelity text-to-vector model with 4MP-tier quality for production-grade SVG assets and detailed illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use this skill to ask an agent to generate vector artwork through the dLazy Recraft V4 Pro Vector CLI wrapper. It is suited for SVG-style production assets, detailed illustrations, and other text-to-vector generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected input files, and generated outputs are sent to dLazy's hosted service.

Mitigation: Use the skill only with data appropriate for the dLazy service, review the service terms, and avoid sending sensitive files unless approved.

Risk: The workflow depends on a third-party CLI package and hosted API endpoints.

Mitigation: Verify trust in the pinned dLazy CLI package before installation, prefer npx for non-persistent use when appropriate, and rotate or revoke the API key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [JSON responses with generated asset URLs, optional downloaded files, and markdown command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated outputs are returned as hosted file URLs and can be saved locally with the CLI --save option.]

## Skill Version(s):

1.3.11 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
