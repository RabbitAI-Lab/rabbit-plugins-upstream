## Description:

Storyblok (storyblok.com). Use this skill for ANY Storyblok request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read Storyblok space, story, datasource, link, and tag data through an OOMOL-connected Storyblok account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes one-line remote installer commands for the oo CLI.

Mitigation: Verify the official installer source, version, and integrity before running installer commands, or use a reviewed installation path.

Risk: The skill relies on OOMOL-mediated access to a Storyblok space.

Mitigation: Install only when OOMOL-mediated access is acceptable for the target Storyblok workspace and account.

Risk: Future connector actions could change Storyblok content or account state.

Mitigation: Treat the current artifact as read-only and require explicit user confirmation before any future write or destructive action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-storyblok)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Storyblok homepage](https://www.storyblok.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
