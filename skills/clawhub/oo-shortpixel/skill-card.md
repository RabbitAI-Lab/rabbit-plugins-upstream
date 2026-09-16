## Description:

ShortPixel (shortpixel.com) handles ShortPixel requests for reading, creating, updating, and deleting data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate ShortPixel through an OOMOL-connected account, including domain association, CDN usage lookup, and cache or storage purge actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may ask users to execute a remote installer script before the installer is verified.

Mitigation: Prefer a verified, versioned oo CLI release or package-manager source; inspect or verify the installer before using pipe-to-shell setup commands.

Risk: Write and destructive ShortPixel domain actions can change account state or purge cached or stored optimized assets.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ShortPixel Homepage](https://shortpixel.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-shortpixel)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live ShortPixel action schemas before payload execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
