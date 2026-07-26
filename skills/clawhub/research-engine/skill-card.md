## Description: <br>
Research-engine automates multi-source research, trend analysis, structured report generation, and staged development-plan drafting for agent workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guogang1024](https://clawhub.ai/user/guogang1024) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to research technical topics across web, GitHub, and Moltbook sources, then turn findings into Markdown reports and short-, mid-, and long-term development plans. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research topics and queries may be sent to external services during web, GitHub, or Moltbook searches. <br>
Mitigation: Use the skill only for topics suitable for external disclosure and avoid submitting sensitive or confidential prompts. <br>
Risk: Recurring or autonomous integrations can repeatedly search external services and accumulate local records. <br>
Mitigation: Enable scheduled use only with explicit limits, review cadence, and clear operator approval. <br>
Risk: Reports and browsing history are written to disk with limited retention and filename controls. <br>
Mitigation: Set RESEARCH_DIR to a controlled location and review generated files before relying on or sharing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/guogang1024/skills/research-engine) <br>
- [Moltbook guogangAgent profile](https://www.moltbook.com/u/guogangAgent) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance] <br>
**Output Format:** [Markdown reports, Python return objects, and command-line status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes research reports and browsing history to RESEARCH_DIR.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata, SKILL.md, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
