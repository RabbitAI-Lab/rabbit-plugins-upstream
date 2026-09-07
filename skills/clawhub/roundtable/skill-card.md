## Description:

Roundtable coordinates Scholar, Engineer, and Muse specialist agents to analyze complex questions in parallel, optionally cross-examine findings, and synthesize a final answer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla)

### License/Terms of Use:

MIT

## Use Case:

Developers, teams, and external users use Roundtable when complex research, architecture, code review, investment, or decision questions benefit from multiple specialist perspectives and a synthesized answer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Council runs can use multiple sub-agents, increasing token cost and latency.

Mitigation: Use quick mode, low-budget presets, or confirmation prompts for exploratory or cost-sensitive tasks.

Risk: Research tasks may use web search, which can expose query context and introduce untrusted source content.

Mitigation: Avoid secrets and sensitive personal, legal, financial, or business data; review cited sources before relying on high-impact answers.

Risk: Session logs may persist user questions and synthesized findings locally.

Mitigation: Disable logging for sensitive work, or review and delete logs in memory/roundtable after use.

Risk: Sub-agent findings can be incomplete, unavailable, or inconsistent.

Mitigation: Use the skill's confidence, dissent, and cross-examination outputs as review signals, and rerun or independently verify high-impact conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/robbyczgw-cla/skills/roundtable)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown responses with optional JSON configuration and local Markdown session logs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use three specialist agent runs in quick mode or six specialist agent runs when Round 2 cross-examination is enabled.]

## Skill Version(s):

0.5.0 (source: frontmatter and changelog, released 2026-08-31)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
