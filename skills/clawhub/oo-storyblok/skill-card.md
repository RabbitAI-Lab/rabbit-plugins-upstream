## Description:

Storyblok (storyblok.com). Use this skill for Storyblok searching and reading tasks through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operators use this skill to retrieve Storyblok space metadata, stories, datasources, links, and tags through an OOMOL-connected account without handling raw Storyblok tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer scripts that may be piped directly into a shell.

Mitigation: Prefer a verified, versioned installer or inspect and verify the installer before execution.

Risk: Storyblok requests and results are routed through OOMOL.

Mitigation: Install only when OOMOL processing of Storyblok requests and returned content is acceptable for the deployment.

## Reference(s):

- [ClawHub Storyblok skill page](https://clawhub.ai/oomol/skills/oo-storyblok)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Storyblok homepage](https://www.storyblok.com)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before running Storyblok read actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
