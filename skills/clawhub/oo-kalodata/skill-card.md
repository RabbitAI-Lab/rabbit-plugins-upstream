## Description:

Kalodata (kalodata.com). Use this skill for ANY Kalodata request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to query Kalodata and TikTok Shop analytics through an OOMOL-connected account. It supports product, creator, category, livestream, shop, video, credit balance, and credit usage workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute code on the user's machine.

Mitigation: Review the oo CLI installation path first and prefer official install instructions, pinned releases, or checksum/signature validation before running installer commands.

Risk: Kalodata actions may query account-linked analytics, credit balances, and credit usage records.

Mitigation: Use an authenticated OOMOL account intentionally connected to Kalodata, fetch the live action schema before each call, and avoid sharing returned account data beyond the user's requested workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-kalodata)
- [Kalodata Homepage](https://www.kalodata.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include account-linked analytics, credit information, and expiring signed media URLs.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
