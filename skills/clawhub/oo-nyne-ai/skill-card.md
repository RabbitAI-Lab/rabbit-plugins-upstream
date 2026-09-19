## Description:

Nyne.ai (nyne.ai). Use this skill for ANY Nyne.ai request -- reading, creating, and updating data. Whenever a task involves Nyne.ai, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Nyne.ai through an OOMOL-connected account, including schema inspection, company and person search, enrichment polling, and usage checks. The skill also guides confirmation before write actions that submit searches or enrichment requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes pipe-to-shell installer commands that execute remote code locally.

Mitigation: Do not run installer commands blindly; use an official version-pinned installer and verify checksums or signatures before installation.

Risk: Write actions can submit Nyne.ai search or enrichment requests and may change service state or consume credits.

Mitigation: Inspect the live action schema, construct the exact payload, and confirm the payload and effect with the user before running any write action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-nyne-ai)
- [Nyne.ai Homepage](https://nyne.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; connector responses are returned as JSON.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
