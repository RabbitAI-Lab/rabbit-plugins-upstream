## Description:

Provides remove.bg actions through OOMOL for checking account credits, removing image backgrounds, and submitting source images for improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to operate a connected remove.bg account from an agent, including checking credits, removing image backgrounds from URL or base64 input, and submitting source images for improvement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute arbitrary local code.

Mitigation: Prefer an official package, pinned release, or verified installer instead of running curl|bash or irm|iex blindly.

Risk: Actions can spend remove.bg credits, upload images, or submit source images for improvement.

Mitigation: Confirm the exact payload and effect before running credit-consuming, upload, write, or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-remove-bg)
- [remove.bg homepage](https://www.remove.bg)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return remove.bg account details, connector execution metadata, or transit-storage links for generated image or ZIP outputs.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
