## Description:

Autonomous deep research agent for multi-step web research, sub-agent delegation, source synthesis, and structured report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lingchenheiye](https://clawhub.ai/user/lingchenheiye)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need comprehensive research, literature reviews, market or competitive analysis, and cited synthesis across multiple web sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad autonomous web fetching may retrieve untrusted or misleading source material.

Mitigation: Review generated citations and conclusions before relying on the report or redistributing it.

Risk: Research topics and fetched content may be sent to external search and LLM services.

Mitigation: Use non-production API keys and avoid confidential, regulated, or internal-only research topics unless that data sharing is approved.

Risk: The backend writes report files with weak path scoping.

Mitigation: Run the skill in a constrained workspace and review or change report paths before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/lingchenheiye/skills/deep-research-engine)
- [Tavily](https://tavily.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with inline citations, plus setup guidance and shell commands when using the standalone backend.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write research request and final report files; requires external search and LLM API keys for full operation.]

## Skill Version(s):

0.1.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
