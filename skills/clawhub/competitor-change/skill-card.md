## Description:

Summarizes observable changes in authorized Amazon competitor product snapshots over supported daily or weekly periods using deterministic diffs and existing review counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and operators use this skill to monitor authorized Amazon competitor products, manage daily or weekly watches, and read deterministic change digests for observed product snapshot fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary says the package includes broader paid analysis and account-changing features beyond the advertised competitor-watch workflow.

Mitigation: Install only when the publisher is trusted with the ARI account, restrict agent use to `python scripts/ari.py watch ...` commands, and request a watch-only build or clearer disclosure before relying on it.

Risk: Paid operations or auto-confirm settings may affect account credits if an agent uses non-watch CLI features.

Mitigation: Review or disable auto-confirm before use and require explicit user confirmation before any paid or account-changing action.

## Reference(s):

- [Amazon 竞品变化监控 专用监控参考](artifact/references/reference.md)
- [Amazon 竞品变化监控 专用监控工作流](artifact/references/watch-workflow.md)
- [ARI service](https://ari.funewa.com)
- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-change)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI response summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Watch digest output is scoped to supported daily or weekly product snapshot monitoring and deterministic summaries.]

## Skill Version(s):

1.4.5 (source: server release evidence, SKILL.md frontmatter, _meta.json, scripts/ari.py VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
