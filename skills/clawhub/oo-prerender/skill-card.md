## Description:

Prerender (prerender.io) access for reading, creating, updating, and deleting Prerender data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Prerender caching workflows from an OOMOL-connected account, including sitemap submission, recaching, cache clearing, and cache-clear status checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI through a verified method and do not let an agent run the remote installer automatically.

Risk: Write and destructive Prerender actions can change or clear cached content.

Mitigation: Confirm the exact payload, target, and intended effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-prerender)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Prerender Homepage](https://prerender.io)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL-connected Prerender credentials and returns connector execution metadata when actions run.]

## Skill Version(s):

1.0.4 (source: server evidence release version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
