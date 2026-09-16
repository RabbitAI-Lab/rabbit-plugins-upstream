## Description:

论衡 orchestrates a multi-agent workflow for research-backed academic papers, long-form analysis, peer review, audit, and publication-channel recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to plan and produce evidence-grounded long-form Chinese or multilingual manuscripts with staged human approvals, multi-agent research, drafting, critique, audit, peer review, and final inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow writes many local project files and status artifacts during normal operation.

Mitigation: Require Phase 0 approval of the project name and file list, keep writes under run/<project>/, and review generated status and audit files before sharing or archiving.

Risk: Depending on Phase 0 choices, research terms, manuscript content, or image prompts may be sent to external providers.

Mitigation: For sensitive or proprietary work, choose the local/no-external option, avoid optional image generation and Firecrawl, and disclose any enabled external service use in the project records.

Risk: Multi-agent research and drafting can still produce incorrect citations, data, or publication advice.

Mitigation: Use the built-in audit, peer-review, final-inspection, and human approval gates, and independently verify high-impact claims before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Quickstart](QUICKSTART.md)
- [Pipeline README](references/pipeline-readme.md)
- [Permissions](references/permissions.md)
- [External Services](references/_shared/external-services.md)
- [Phase Order](references/_shared/phase-order.yaml)
- [Asset Index](references/_shared/asset-index.md)
- [Deliverables](references/deliverables.md)
- [G14 Chinese AI Trace Gate](references/gates/14-中文AI痕迹-gate.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Configuration, Text, Files]

**Output Format:** [Markdown and structured project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create status, draft, audit, report, and delivery files under run/<project>/ after explicit Phase 0 approval.]

## Skill Version(s):

2.12.48 (source: metadata.openclaw.version and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
