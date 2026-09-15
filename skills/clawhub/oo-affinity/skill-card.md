## Description:

Affinity enables agents to search and read Affinity CRM data through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Affinity CRM companies, people, opportunities, lists, saved views, and field metadata through an authenticated OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documentation includes commands that directly execute remote installer scripts.

Mitigation: Prefer an official package manager, a versioned installer, or a manually downloaded installer with verification where available.

Risk: The skill routes Affinity access through OOMOL and depends on the user's connected Affinity data.

Mitigation: Install only when the user trusts OOMOL with the Affinity data connected to the account.

Risk: Future write or destructive Affinity actions could change or remove CRM data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before allowing any write or destructive action.

## Reference(s):

- [ClawHub Affinity skill page](https://clawhub.ai/oomol/skills/oo-affinity)
- [Affinity homepage](https://www.affinity.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output from connector actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses include data and execution metadata when actions are run.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
