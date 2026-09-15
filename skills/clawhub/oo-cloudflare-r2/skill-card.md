## Description:

Cloudflare R2 helps agents read, create, update, and delete Cloudflare R2 resources through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cloudflare R2 buckets, objects, domains, lifecycle rules, CORS policies, event notifications, credentials, metrics, and related account resources from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts for the oo CLI.

Mitigation: Install only when the publisher is trusted, and prefer a verified or package-manager installation path when available.

Risk: The skill can run write and destructive Cloudflare R2 actions that alter or remove buckets, objects, domains, CORS policies, lifecycle rules, event notifications, and related resources.

Mitigation: Confirm the exact target, payload, and effect with the user before running any action tagged write or destructive.

Risk: Custom domains, Queue notifications, presigned URLs, and temporary credentials can expose or change account resources.

Mitigation: Review requested scope, expiration, public access, and destination settings before creating or updating these resources.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-cloudflare-r2)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Cloudflare R2](https://www.cloudflare.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; state-changing and destructive actions require user confirmation.]

## Skill Version(s):

1.0.9 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
