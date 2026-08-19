## Description:

Prepares final sn-deep-research Markdown by converting footnote citation keys into numbered references, deduplicating source URLs, inserting optional L0 and table-of-contents sections, and appending a bibliography.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research-report agents use this skill after draft assembly to convert evidence-backed footnote IDs into numbered references, repair claim-ID citation leakage where evidence supports it, and produce a publishable Markdown report with citation metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Legacy mode can overwrite the input report when --output is omitted.

Mitigation: Prefer the documented --output workflow so the original stitched.md remains intact, then review report.md and citations.json before publishing.

Risk: Unresolved orphan citations or claim-ID leakage can leave unsupported citation markers in the final report.

Mitigation: Treat non-empty orphan_citations or unresolved claim_id_leakage in stdout as blockers and route the draft back for citation repair before delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-prepare-citations)
- [artifact/SKILL.md](artifact/SKILL.md)
- [artifact/scripts/prepare_citations.py](artifact/scripts/prepare_citations.py)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Processed Markdown report, citations.json, and structured JSON status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report orphan citations, claim-ID leakage repair results, L0 insertion state, and table-of-contents status.]

## Skill Version(s):

2026.8.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
