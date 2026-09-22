## Description:

Generates vector-style design assets such as logos and icons from text prompts using dLazy's hosted Recraft V4 Vector workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request scalable design assets from text prompts through the dLazy CLI. It is suited for logo, icon, and other design-asset generation workflows that can use hosted image-generation services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied local media may be sent to dLazy hosted endpoints.

Mitigation: Avoid submitting confidential or regulated content unless the user's organization has approved dLazy's service terms and data handling.

Risk: The dLazy CLI can store an API key in the local user configuration.

Mitigation: Use per-run DLAZY_API_KEY for ephemeral credentials when preferred, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: The skill describes SVG/vector output, while the artifact's example response shows a PNG result.

Mitigation: Verify the returned MIME type and downloaded file format before relying on the output in vector-only production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Guidance]

**Output Format:** [JSON response with generated asset URLs; optional saved generated asset file via CLI flags]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses prompt and aspect-ratio inputs; asynchronous mode can return a generateId for later polling.]

## Skill Version(s):

1.3.17 (source: server release evidence; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
