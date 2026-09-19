## Description:

专利查新与可专利性判断。当用户问一个技术方案有无在先公开、是否适合申请专利、是否需要申请前查新或立项前方向筛查时使用；requires a PatentMax API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, patent teams, and technical reviewers use this skill to prepare paid PatentMax novelty checks, compare prior-art references against a technical solution, interpret quality-limited results, and generate deliverable patent novelty report outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive invention details and the PatentMax API key can be sent to the configured PatentMax endpoint, and server evidence flags redirect risk through PATENTMAX_BASE_URL.

Mitigation: Run from a trusted shell, keep PATENTMAX_BASE_URL unset unless deliberately testing a trusted endpoint, use a limited or test API key when possible, and avoid submitting undisclosed core formulas or parameters unless that confidentiality risk is acceptable.

Risk: Patent novelty reports can be mistaken for official or guaranteed patentability conclusions.

Mitigation: Frame outputs as bounded technical references, state search scope and quality limits, and require qualified patent or official novelty-search review for formal decisions.

Risk: Paid novelty checks can be wasted or duplicated when the technical solution is too vague or a long-running task is resubmitted.

Mitigation: Confirm cost and user intent before execution, require enough implementation detail, use the built-in idempotency behavior, and resume long-running tasks with status rather than creating duplicates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ip930/skills/patentmax-novelty)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [PatentMax API](https://api.ip930.com)
- [技术方案怎么写](references/solution-guide.md)
- [专利查新工作流](references/workflow.md)
- [排查](references/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell command examples, JSON command output, and optional DOCX report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PATENTMAX_API_KEY; create/status/download commands call the PatentMax API and may process sensitive invention details.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
