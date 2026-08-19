## Description:

Target Discovery analyzes compound SMILES through ADMET filtering, scaffold analysis, structure-similarity search, target validation, FTO patent risk scanning, and SAR extraction to prioritize target-compound optimization directions and optional PPT/PDF reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Life-science researchers, pharmaceutical teams, CROs, and developers use this skill to reverse-discover likely molecular targets from compound libraries and prioritize validation, patent-risk, and SAR follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential compound SMILES and research questions may be sent to configured PatSnap/OpenClaw services.

Mitigation: Use only after confirming the user's data-handling requirements and the configured service authorization posture.

Risk: Target, FTO, patent, medical, and SAR outputs are research support and may be incomplete or unsuitable for legal or clinical decisions.

Mitigation: Require expert scientific, legal, and clinical review before acting on generated conclusions.

Risk: The workflow depends on external MCP services for live chemical, patent, and SAR retrieval.

Mitigation: Confirm required services are installed, active, and authorized before running the full workflow; otherwise limit output to process guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/target-discovery)
- [PatSnap Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration, Guidance]

**Output Format:** [Markdown analysis report with optional PPT/PDF report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source markers for target, patent, and literature conclusions; live results depend on configured PatSnap/OpenClaw services.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
