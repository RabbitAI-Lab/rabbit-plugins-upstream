## Description: <br>
Memory Radar helps agents scan AI memory files and workspace configuration for prompt injection, credential exposure, data-exfiltration instructions, and related security risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to audit agent memory and configuration files before continued use, after importing external content, or before sharing context across agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote LLM analysis may transmit portions of memory content outside the local environment. <br>
Mitigation: Use the default local mode for routine scans and require explicit approval before enabling remote analysis. <br>
Risk: Quarantine, restore, or scheduled-scan setup can modify files or create persistent local state. <br>
Mitigation: Review the proposed changes before allowing quarantine actions or scheduled monitoring to run. <br>


## Reference(s): <br>
- [Memory Radar ClawHub listing](https://clawhub.ai/thcjp/skills/memory-radar) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and optional JSON scan reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local scan recommendations, optional remote LLM analysis, quarantine and restore steps, and scheduled scan setup.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
