## Description:

Evaluates technology, AI, data, cloud, and enterprise-software topic portfolios by normalizing inputs, applying evidence and originality gates, scoring eligible topics, and preparing portfolio decisions with Notion change previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Editors, analysts, and content strategists use this skill to review a batch of candidate topics, choose one primary topic and two backups, and assign merge, watch, short-note, covered-track, or abandon decisions. It is especially suited to recurring editorial planning where topic evidence, timeliness, originality, portfolio balance, and private Notion writeback boundaries must be reviewed before action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Standing Notion auto-sync instructions could allow unintended database updates if they are stale or broader than the current review.

Mitigation: Confirm that any standing sync authorization is current, explicit, and limited to the intended database, page set, and fields before using it.

Risk: Notion credentials, database identifiers, field mappings, or private topic notes could be exposed through reusable skill files or generated reports.

Mitigation: Keep credentials and private mappings in secure environment variables or private configuration, and avoid including private notes in public templates or generic skill outputs.

Risk: A generated writeback preview could contain incorrect status, priority, or evaluation-field changes.

Mitigation: Review the change preview and approved change set before writeback, require explicit portfolio and writeback confirmation, and verify results through readback comparison.

Risk: Bundled Notion write mode is intentionally incomplete and should not be treated as a production writeback implementation.

Mitigation: Use a separate reviewed write adapter for real writeback, driven by approved page-level change sets and dry-run safeguards.

## Reference(s):

- [Evaluation Gates](references/evaluation-gates.md)
- [Scoring Model](references/scoring-model.md)
- [Portfolio Rules](references/portfolio-rules.md)
- [Notion Adapter Interface](references/notion-adapter-interface.md)
- [Replay Evaluation](references/replay-evaluation.md)
- [ClawHub Skill Release](https://clawhub.ai/haiyangchenbj/skills/editorial-topic-portfolio-skill)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON topic records and change sets, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces gate results, scores, portfolio decisions, change previews, validation output, optional dry-run/readback records, and handoff guidance.]

## Skill Version(s):

1.0.5 (source: evidence.release.version, target metadata, and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
