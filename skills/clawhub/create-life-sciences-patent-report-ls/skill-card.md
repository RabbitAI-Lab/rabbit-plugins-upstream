## Description:

Create or update traceable, self-contained HTML patent intelligence reports for life-sciences technologies, targets, drugs, antibodies, ADCs, companies, or patent sets, integrating patent, scientific, clinical, commercial, and inline figure evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, life-sciences business teams, and technical reviewers use this skill to prepare evidence-traceable patent landscape or deep-dive reports. It supports structured analysis of claims, family status, technical features, experiments, pipeline and clinical context, literature, deals, news, and patent figure evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive sequences, figures, patent strategy, or business data could be shared with external services or written to an unsuitable output location.

Mitigation: Confirm which PatSnap MCPs and output locations are approved before use, and avoid confidential inputs unless the selected services and storage location are authorized.

Risk: Patent, clinical, or commercial evidence could be misread as legal advice, independent experimental validation, or proof of license or ownership scope.

Mitigation: Keep patent, scientific, clinical, regulatory, and commercial evidence visibly separate, cite source IDs for material claims, and route FTO, validity, enforceability, or license-scope questions to qualified counsel.

Risk: Incorrect or invented links could weaken traceability in the generated report.

Mitigation: Use exact returned URLs or verified primary-source URLs, preserve source identifiers, and reject guessed routes or mismatched identifier parameters during link audit.

## Reference(s):

- [Life Sciences Patent Report Specification](references/report-spec.md)
- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/create-life-sciences-patent-report-ls)
- [PatSnap patent search MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap patent briefing MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [PatSnap target disease MCP server](https://open.patsnap.com/marketplace/mcp-servers/target-disease)
- [PatSnap drug asset MCP server](https://open.patsnap.com/marketplace/mcp-servers/drug-asset)
- [PatSnap clinical trials MCP server](https://open.patsnap.com/marketplace/mcp-servers/clinical-trials)
- [PatSnap scientific translational evidence MCP server](https://open.patsnap.com/marketplace/mcp-servers/scientific-translational-evidence)
- [PatSnap regulatory guidelines MCP server](https://open.patsnap.com/marketplace/mcp-servers/regulatory-guidelines)
- [PatSnap current awareness MCP server](https://open.patsnap.com/marketplace/mcp-servers/current-awareness)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Self-contained HTML report with source registers, evidence tables, audit notes, and inline figure citations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source identifiers, exact returned URLs, retrieval details, confidence notes, and omitted-module rationale.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
