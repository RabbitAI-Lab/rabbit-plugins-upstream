## Description:

Webflow (webflow.com). Use this skill for Webflow requests involving reading, creating, updating, publishing, and deleting site or CMS data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Webflow schemas and run Webflow site and CMS actions through an OOMOL-connected account. It supports reads, creates, updates, publishes, and deletes, with confirmation expected before state-changing or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that execute shell or PowerShell code.

Mitigation: Prefer a versioned, verifiable oo CLI installation method when available, and review installer contents before running remote scripts.

Risk: Write, publish, and delete actions can change Webflow site or CMS state.

Mitigation: Inspect the live action schema, use least-privilege Webflow access, and confirm the exact target, payload, and expected effect before approving state-changing actions.

Risk: Connector use depends on an OOMOL-connected account and server-side Webflow credentials.

Mitigation: Confirm the connected account, scopes, and billing state before use, and avoid handling raw Webflow tokens directly.

## Reference(s):

- [ClawHub Webflow skill page](https://clawhub.ai/oomol/skills/oo-webflow)
- [Webflow homepage](https://webflow.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
