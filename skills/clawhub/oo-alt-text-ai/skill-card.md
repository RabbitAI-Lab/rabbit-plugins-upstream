## Description:

Operate AltText.ai through an OOMOL-connected account to read image data, generate alt text, scrape pages for images, and delete image records when explicitly approved.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operators use this skill to inspect AltText.ai account and image records, generate alt text for publicly accessible image URLs, scrape pages for images, and manage image library entries through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands executed directly in a shell.

Mitigation: Install the oo CLI only from reviewed official documentation or a verified package-manager flow before using the skill.

Risk: The skill can create AltText.ai image records and delete existing image records.

Mitigation: Confirm the exact payload and intended effect before create actions, and require explicit approval for delete actions.

Risk: The skill depends on OOMOL-connected account credentials and the oo CLI provider path.

Mitigation: Use the skill only when the user is comfortable with OOMOL as the CLI provider and the AltText.ai account connection is expected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-alt-text-ai)
- [AltText.ai Homepage](https://alttext.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces oo CLI commands and connector payload guidance; command responses are JSON when --json is used.]

## Skill Version(s):

1.0.4 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
