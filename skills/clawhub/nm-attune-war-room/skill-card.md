## Description:

Convenes a multi-LLM expert panel to pressure-test hard-to-reverse decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical decision makers use this skill to route high-stakes architecture, strategy, and implementation choices through reversibility scoring, multi-expert deliberation, adversarial review, premortem analysis, and final decision synthesis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive decision context may be stored locally or published to GitHub Discussions by the skill workflow.

Mitigation: Before using the skill on confidential work, disable or decline discussion publishing and review any generated summaries before they leave the environment.

Risk: Decision context may be sent to external LLM tools during multi-expert deliberation.

Mitigation: Use approved model providers and avoid submitting confidential, regulated, or customer-sensitive material unless data handling has been reviewed.

Risk: The artifact describes a GLM fallback command that bypasses normal permission prompts.

Mitigation: Avoid that fallback unless it has been explicitly approved, or replace it with a permission-preserving execution path.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-attune-war-room)
- [Clawdis Homepage Metadata: claude-night-market attune](https://github.com/athola/claude-night-market/tree/master/plugins/attune)
- [Farnam Street: Reversible and Irreversible Decisions](https://fs.blog/reversible-irreversible-decisions/)
- [Tapan Desai: One-Way and Two-Way Door Decision-Making](https://tapandesai.com/one-way-two-way-doors-decision-making/)
- [Ashik Uzzaman: Amazon's Type 1 vs Type 2 Decisions](https://ashikuzzaman.com/2025/03/03/amazons-type-1-vs-type-2-decisions-a-framework-for-effective-decision-making/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown decision documents with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces reversibility assessments, expert-panel analyses, decision records, implementation orders, watch points, reversal plans, dissenting views, and optional session artifacts.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
