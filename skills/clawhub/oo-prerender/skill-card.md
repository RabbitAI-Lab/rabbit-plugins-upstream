## Description:

Prerender helps agents operate Prerender through an OOMOL-connected oo CLI account for reading data and performing cache-related actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Prerender through OOMOL-connected CLI workflows, including inspecting action schemas, submitting sitemaps, clearing caches, checking cache-clear status, and recaching URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands may execute unreviewed installation scripts.

Mitigation: Prefer an official package or a verified installer source before installing the oo CLI, and do not run remote install commands blindly.

Risk: Prerender cache operations can change account state or clear cached content.

Mitigation: Confirm the exact payload, target URLs or wildcard pattern, and expected effect with the user before running write or destructive actions.

Risk: Recaching URLs may consume Prerender service resources.

Mitigation: Require explicit confirmation before recaching URLs and keep the submitted URL set scoped to the user's request.

## Reference(s):

- [ClawHub Prerender Skill Page](https://clawhub.ai/oomol/skills/oo-prerender)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Prerender Homepage](https://prerender.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash, PowerShell, text, and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are intended for the oo CLI and connector actions may return JSON responses.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
