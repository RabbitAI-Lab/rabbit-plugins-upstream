## Description:

Audit catalyst preparation and evaluation methods for executability, reproducibility, controlled comparison, attribution, measurement reliability, safety-review readiness, and claim-to-evidence linkage. Use for experimental procedures, screenshots, paper methods, patent examples, draft plans, and machine-generated catalyst routes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Research scientists, principal investigators, project leads, and technical reviewers use this skill to audit catalyst preparation and evaluation methods before experiments or review. It turns procedures, paper methods, patent examples, screenshots, draft R&D concepts, or machine-generated catalyst routes into structured findings about executability, reproducibility, comparison design, measurement reliability, safety-review readiness, and claim support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated audit reports may contain confidential experimental material from user-provided inputs.

Mitigation: Use a dedicated output folder and retain or share generated JSON, HTML, and Word reports according to the input material's confidentiality requirements.

Risk: External patent or scientific lookups could mix retrieved evidence with submitted method facts or disclose sensitive context.

Mitigation: Use external services only with explicit authorization and keep retrieved evidence separate from the submitted method record.

Risk: Readers could mistake the audit for result authentication, safety approval, regulatory clearance, patentability analysis, or specialist review.

Mitigation: Treat the output as technical method-development guidance and route hazards, pressure equipment, toxic gases, waste, and institutional requirements to qualified EHS and laboratory reviewers.

Risk: Writing reports into an unsafe or shared directory can overwrite or expose unrelated files.

Mitigation: Run the generator with a dedicated output directory and validate outputs before use; the included scripts refuse root-like output paths and symbolic-link outputs.

## Reference(s):

- [Audit methodology](artifact/references/methodology.md)
- [ClawHub skill release](https://clawhub.ai/yuanzhian-patsnap/skills/audit-catalyst-experimental-methods-rd)
- [PatSnap patent search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap patent briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance and shell commands that generate JSON, HTML, and DOCX report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The deterministic entry point writes report_context.json, an HTML report, and a Word report to a dedicated output directory, then validates the generated artifacts.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact VERSION is 0.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
