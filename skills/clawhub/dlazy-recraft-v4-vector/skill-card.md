## Description:

Helps agents generate logo, icon, and design assets from text prompts through the dLazy Recraft V4 Vector CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to ask an agent to generate logos, icons, and other design assets from prompts, with optional aspect ratios and local downloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external CLI and sending prompts or supplied media to dLazy exposes content to a third-party service.

Mitigation: Review the pinned CLI dependency and avoid submitting sensitive prompts or files without approval.

Risk: The login flow saves an API key locally.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials when local key storage is unsuitable.

Risk: The documented result example is PNG although the skill describes SVG output.

Mitigation: Check the returned asset's MIME type and format before treating it as editable vector artwork.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [dLazy CLI repository (declared in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns an asset URL and MIME type; its example shows PNG despite the SVG description. An optional save path downloads the asset.]

## Skill Version(s):

1.3.22 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
