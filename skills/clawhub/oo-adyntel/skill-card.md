## Description:

Adyntel (adyntel.com). Use this skill for ANY Adyntel request - searching and reading data. Whenever a task involves Adyntel, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to query Adyntel through OOMOL-managed connector actions for ad-library searches, TikTok ad details, and paid or organic keyword metrics. It is intended for read-only competitive advertising and keyword research through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell installer commands, and the security scan marks the release as suspicious for that setup behavior.

Mitigation: Review the setup path before installation, prefer a trusted package manager or verified release, and do not run remote installer commands unless the source has been independently reviewed and trusted.

Risk: Connector actions depend on live schemas and OOMOL-managed credentials, so stale assumptions can produce incorrect requests.

Mitigation: Fetch the authoritative action schema with the oo CLI before constructing each payload and rely on OOMOL-managed credentials rather than handling raw tokens.

## Reference(s):

- [Adyntel homepage](https://www.adyntel.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-adyntel)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector action schemas before running read-only Adyntel calls.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
