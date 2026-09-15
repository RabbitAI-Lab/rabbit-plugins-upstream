## Description:

Kalodata lets an agent search and read TikTok commerce analytics for categories, creators, livestreams, products, shops, and videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to query Kalodata analytics for TikTok categories, creators, livestreams, products, shops, and videos through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell installer commands and the security verdict is suspicious.

Mitigation: Review the oo CLI installation path first and prefer a pinned, verified release or trusted package manager before using the skill.

Risk: Queries run through the user's OOMOL-connected Kalodata account.

Mitigation: Confirm the intended account connection, scopes, and billing status before retrying authentication, connection, or HTTP 402 failures.

## Reference(s):

- [Kalodata homepage](https://www.kalodata.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kalodata)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches the live action schema before constructing request payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
