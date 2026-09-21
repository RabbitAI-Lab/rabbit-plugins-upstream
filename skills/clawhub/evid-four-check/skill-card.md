## Description:

A zero-dependency CLI that provides decision support for reviewing the authenticity, legality, relevance, and integrity of electronic evidence under cited Chinese court rules and returns JSON IR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, compliance teams, and legal operations users can run the CLI to structure a preliminary four-characteristics review of electronic evidence. The output is decision support only and requires qualified human review before relying on any legal conclusion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool may produce incorrect or outdated legal decision-support conclusions if laws, court rules, or user-provided facts are incomplete or stale.

Mitigation: Verify current official legal texts and require qualified human review before relying on conclusions.

Risk: Users may mistake the JSON classification for legal advice or a compliance proof.

Mitigation: Present the output as preliminary decision support and preserve the artifact's disclaimer that final acceptance is determined by the relevant authority.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zhaoxinghua09-cell/skills/evid-four-check)
- [LGD Theory Ledger](https://medxpert.cn/theory)

## Skill Output:

**Output Type(s):** [JSON, Guidance, Shell commands]

**Output Format:** [JSON IR from a local CLI, with documentation examples in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes rc status codes and AIGC metadata; no network, credential, persistence, or system-modifying behavior is reported by security evidence.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
