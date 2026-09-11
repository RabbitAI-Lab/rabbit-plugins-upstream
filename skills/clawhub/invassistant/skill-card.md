## Description:

InvAssistant is a multi-asset portfolio management skill for US, A-share, and HK stocks, with asset classification, red-line risk controls, QMS scoring, and disciplined entry and exit guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill as investment decision support: reviewing portfolio concentration, classifying holdings, evaluating candidate entries or exits, and generating disciplined risk-control reports. It is not tax, legal, regulatory, or individualized financial advice, and trade-related outputs require human review before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make lasting changes to portfolio configuration, reports, and agent memory.

Mitigation: Review every proposed write before allowing it, and keep account numbers, broker credentials, and other sensitive identifiers out of runtime files.

Risk: Optional webhook adapters can send sensitive portfolio reports to external messaging services.

Mitigation: Keep webhook adapters disabled unless needed, store webhook secrets outside shared files, and review report content before enabling push delivery.

Risk: Buy, sell, reduce, and hold signals may be mistaken for executable trading instructions.

Mitigation: Treat all signals as informational decision support and require human review before any trade execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/invassistant)
- [README](README.md)
- [US Stock Strategy](references/us_stock_strategy.md)
- [A-Share Strategy](references/a_share_strategy.md)
- [Risk Control and Overrides](references/risk_control_and_overrides.md)
- [Candidate Admission Gates](references/candidate_admission_gates.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance, JSON portfolio reports, generated configuration files, shell commands, and optional webhook notifications.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-supplied portfolio configuration and market data; can persist configuration, report, and runtime-memory updates; webhook adapters should remain disabled unless explicitly configured.]

## Skill Version(s):

2.3.14 (source: server release metadata and SKILL.md frontmatter, released 2026-09-11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
