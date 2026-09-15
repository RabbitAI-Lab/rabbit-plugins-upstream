## Description:

Mindbody (mindbodyonline.com). Use this skill for ANY Mindbody request -- searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect the Mindbody connector schema and list Mindbody businesses through an OOMOL-connected account without handling raw credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that execute immediately in the shell.

Mitigation: Prefer a verified package-manager or otherwise trusted installation path for the oo CLI before using the skill.

Risk: Using the connector requires an OOMOL-connected Mindbody account with credentials handled server-side.

Mitigation: Connect Mindbody only after reviewing OOMOL account and credential handling requirements.

## Reference(s):

- [Mindbody homepage](https://www.mindbodyonline.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mindbody)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mindbody action results are returned by the oo CLI as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
