## Description: <br>
Deep Research Pro helps agents search public web sources, synthesize findings, and deliver cited research reports without paid API keys. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to turn a research request into a multi-source web investigation with cited findings, summaries, and saved reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research prompts may expose sensitive internal topics through outbound web searches. <br>
Mitigation: Avoid secrets and sensitive internal topics in prompts, and keep results in chat when files should not be written locally. <br>
Risk: The skill can save local research reports under ~/clawd/research. <br>
Mitigation: Review the output path and use chat-only delivery when local retention is not desired. <br>
Risk: Public web sources may be inaccurate, stale, or inconsistent. <br>
Mitigation: Require citations, cross-check important claims, and flag unsupported or single-source findings. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/seanford/skills/deep-research-pro) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>
- [uv](https://github.com/astral-sh/uv) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown research reports, chat summaries, optional JSON, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save reports under ~/clawd/research/[slug]/report.md; results depend on public web sources and DuckDuckGo search availability.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
