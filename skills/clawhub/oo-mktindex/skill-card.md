## Description:

Moojing Market Intelligence lets agents use OOMOL's mktindex connector to read, create, update, and delete Moojing market intelligence and monitoring data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run Moojing market, category, brand, item, shop, regional, and price-monitoring workflows through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes remote installer fallback commands for the oo CLI.

Mitigation: Before installing, review the oo CLI installer source or use a trusted installation method where available.

Risk: Write and destructive Moojing actions can change or remove account data.

Mitigation: Confirm the exact action, target, and JSON payload with the user before running write or destructive actions.

## Reference(s):

- [Moojing Market Intelligence homepage](https://www.mktindex.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Moojing ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mktindex)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
