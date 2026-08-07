## Description: <br>
八字操作系统 guides an agent through BaZi birth-chart analysis using a nine-layer diagnostic workflow, cross-school validation, classical-source tracing, and structured Markdown reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yhc2026](https://clawhub.ai/user/yhc2026) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users use this skill to collect birth date, exact time, birthplace, and gender, then generate a structured BaZi analysis report with chart verification, diagnostic layers, confidence notes, and classical references. It is intended as astrology-style interpretive guidance, not factual prediction or professional advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow collects birth date, exact time, birthplace, gender, and possibly a name. <br>
Mitigation: Use a pseudonym when possible and only provide this data if the user is comfortable with the workflow handling it. <br>
Risk: The skill saves local Markdown reports that may include sensitive personal inferences. <br>
Mitigation: Review or disable report saving where possible, and delete reports that should not be retained. <br>
Risk: The skill can generate health, fertility, relationship, family, and life-decision predictions from birth data. <br>
Mitigation: Treat outputs as astrology-style interpretation and do not rely on them as factual findings or professional advice. <br>
Risk: Using the source directly with Claude Code may enable local settings permissions for Git or WebSearch. <br>
Mitigation: Review local settings permissions before enabling or running the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yhc2026/skills/bazi-os) <br>
- [Publisher profile](https://clawhub.ai/user/yhc2026) <br>
- [Project homepage](https://github.com/bazi-os/bazi-os) <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [BaZi analysis command](artifact/.claude/skills/bazi.md) <br>
- [Top-level reasoning framework](artifact/框架/顶级命理师思维框架.md) <br>
- [Analysis template](artifact/框架/排盘分析模板.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance, Files] <br>
**Output Format:** [Structured Markdown report saved as a local .md file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Collects sensitive birth details and may save named reports under the output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
