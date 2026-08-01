## Description: <br>
A Chinese-language research workflow that guides agents through multi-source information gathering, source evaluation, conflict reconciliation, and structured report generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Students, personal researchers, and developers use this skill to conduct bounded research tasks, compare sources, assess credibility, and produce concise structured research reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The trigger text can route unrelated SEO or ranking-improvement requests into a networked, exec-capable research workflow. <br>
Mitigation: Review and narrow the trigger wording before deployment so SEO manipulation requests are not routed to this skill. <br>
Risk: The artifact includes command-line examples but no actual script file, which may cause users or agents to improvise execution behavior. <br>
Mitigation: Treat the commands as illustrative unless a reviewed implementation script is supplied, and require review before executing generated commands. <br>
Risk: Research topics and search terms may be sent to external search engines or news sites. <br>
Mitigation: Avoid sensitive topics unless approved for external research, and disclose which external services receive the topic before running networked searches. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/in-depth-research-tool-free) <br>
- [Artifact SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown research reports with source lists, confidence notes, methodology notes, and optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Free edition states a standard-depth limit of up to 15 sources for a single research task.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
