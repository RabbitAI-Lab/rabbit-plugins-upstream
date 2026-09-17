## Description:

Beehiiv (beehiiv.com). Use this skill for ANY Beehiiv request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Beehiiv publications, posts, and subscriptions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends remote installer execution for the oo CLI.

Mitigation: Prefer a verified or package-managed oo CLI installation before using the Beehiiv connector.

Risk: Beehiiv account data, including subscriber and post information, is routed through OOMOL.

Mitigation: Use the skill only when OOMOL is an acceptable intermediary and keep requests scoped to the specific publication, post, or subscription needed.

## Reference(s):

- [ClawHub Beehiiv skill](https://clawhub.ai/oomol/skills/oo-beehiiv)
- [Beehiiv homepage](https://www.beehiiv.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before running Beehiiv actions.]

## Skill Version(s):

1.0.4 (source: release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
