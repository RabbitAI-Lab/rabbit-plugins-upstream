## Description:

Analyzes fixed multi-zone home camera video for solo-living elder activity and raises a long-term no-activity alert when no movement is detected for the configured window, defaulting to 12 hours.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, community elder-care operators, and developers integrating elder-safety monitoring workflows use this skill to analyze home camera files or URLs for prolonged inactivity and produce alerts, structured reports, and report links. It is an auxiliary monitoring tool and does not provide medical diagnosis or rescue instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home video and report history are sent through cloud APIs.

Mitigation: Use only with consent from the monitored person or authorized caregivers, and avoid visual monitoring in sensitive areas when a less invasive sensor can satisfy the use case.

Risk: Local workspace data may contain identity records and tokens.

Mitigation: Treat the workspace data directory as sensitive, restrict access, apply retention controls, and prefer an explicit managed account over silent default identity behavior.

Risk: A long-term no-activity alert may be incorrect, delayed, or incomplete.

Mitigation: Use alerts as auxiliary monitoring signals, require human verification, and do not treat the output as medical diagnosis or a rescue plan.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-long-term-immobility-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API error-code reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured report text, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include activity timestamps, idle duration, active zones, alert levels, suggested contacts, and report links; history queries return Markdown tables.]

## Skill Version(s):

1.0.8 (source: server release evidence; artifact SKILL.md frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
