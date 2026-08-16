## Description:

Generate and prioritize experimentally testable target hypotheses from one or more small-molecule structures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, discovery teams, and agent users use this skill to turn SMILES, SDF/MOL records, or compound libraries into evidence-backed target hypotheses, SAR summaries, patent review questions, and prioritized validation experiments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Compound structures may be confidential or controlled by data-sharing agreements.

Mitigation: Use the skill only with services the user is authorized to access and confirm authorization before sharing structures externally.

Risk: Target rankings, ADMET signals, SAR interpretations, and patent screens can be mistaken for proof or professional advice.

Mitigation: Treat outputs as hypothesis-generation support, keep uncertainty visible, and confirm target engagement, safety, developability, and legal conclusions through qualified experimental or professional review.

Risk: Missing chemistry-service coverage can create unsupported claims about ADMET, scaffold analysis, similarity search, patent-structure retrieval, or automated SAR extraction.

Mitigation: Use those capabilities only when an authorized service is actually available; otherwise request user exports or report a protocol and explicit coverage gap.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/prioritize-drug-targets-ls)
- [PatSnap patent search MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap patent briefing MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [PatSnap target disease MCP server](https://open.patsnap.com/marketplace/mcp-servers/target-disease)
- [PatSnap drug asset MCP server](https://open.patsnap.com/marketplace/mcp-servers/drug-asset)
- [PatSnap clinical trials MCP server](https://open.patsnap.com/marketplace/mcp-servers/clinical-trials)
- [PatSnap scientific translational evidence MCP server](https://open.patsnap.com/marketplace/mcp-servers/scientific-translational-evidence)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report with structured tables; optional PDF or PPTX when requested and supported]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes evidence grading, source IDs, uncertainty, limitations, validation steps, and patent-review questions.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
