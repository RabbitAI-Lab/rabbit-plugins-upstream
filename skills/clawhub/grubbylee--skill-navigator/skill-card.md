## Description: <br>
Use when users ask which already-installed local Agent Skill should handle a task. It calls local skm recommendations from the real installed skill catalog; it does not perform the task itself. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[grubbylee](https://clawhub.ai/user/grubbylee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to choose the best already-installed local Agent Skill for a described task. It recommends 1-3 installed skills from the local skm catalog and explains why they fit. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on aide-skill-manager and a local skm catalog of installed Claude or Codex skills. <br>
Mitigation: Install only if that local catalog maintenance is acceptable, and refresh recommendations with skm scan after installing or removing skills. <br>
Risk: The skm output is documented as Chinese-first, which can reduce usability for non-Chinese users. <br>
Mitigation: Ask the agent to summarize recommendations in the preferred language when needed. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/grubbylee/skills/skill-navigator) <br>
- [skill-manager project homepage](https://github.com/GrubbyLee/skill-manager) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and concise recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Recommendations are based on the local skm catalog; stale catalogs should be refreshed with skm scan.] <br>

## Skill Version(s): <br>
0.1.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
