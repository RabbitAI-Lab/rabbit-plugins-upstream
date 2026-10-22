## Description:

Drafts a seven-section investment committee memo from a company identifier or supplied materials, linking figures to sources and flagging missing data for human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Investment analysts and deal teams use the skill to organize pre-investment materials into an internal discussion draft with traceable figures, opposing arguments, and unresolved data gaps. It does not provide ratings, valuations, trading recommendations, or final decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Cue connections may expose the API key or transmit confidential files.

Mitigation: Prefer local drafting until credentials are restricted to approved HTTPS destinations; approve which files may be sent and redact confidential material.

Risk: Memo checks may accept missing evidence and do not establish that citations or claims are factually correct.

Mitigation: Manually verify each figure against its cited source, confirm both sides of the argument, and review unresolved gaps even when checks pass.

Risk: Optional dependencies may introduce supply-chain risk.

Mitigation: Review and pin optional dependencies before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huhoo/skills/cue-ic-memo-cn)
- [Publisher profile](https://clawhub.ai/user/huhoo)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Markdown, JSON, JSONL]

**Output Format:** [A seven-section investment committee memo in Markdown, accompanied by a run-account JSON file and source-index records.]

**Output Parameters:** [1D (one company per memo run)]

**Other Properties Related to Output:** [Draft only; intended to present both supporting and opposing evidence and identify data gaps. Checks validate format, not factual accuracy; no ratings, valuations, trading recommendations, or final decisions.]

## Skill Version(s):

0.3.1 (source: frontmatter, changelog; released 2026-10-22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
