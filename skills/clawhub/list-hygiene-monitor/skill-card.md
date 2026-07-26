## Description: <br>
List Hygiene Monitor helps agents monitor email list health over time by reading engagement, bounce, complaint, and suppression evidence to produce decay cohorts and a segmented re-permission, sunset, and prune worklist. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, lifecycle, and email operations users use this skill to run recurring list-hygiene checks between sends, identify engagement decay and suppression drift, and prepare a reviewed worklist for re-permissioning, sunsetting, or pruning subscribers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read email engagement exports, bounce and complaint data, suppression history, and other subscriber-level operational data. <br>
Mitigation: Install and run it only where the agent is permitted to access those exports, and treat exported subscriber or suppression-list content as untrusted data. <br>
Risk: The skill produces prune, sunset, and suppression recommendations that could affect active email lists if applied without review. <br>
Mitigation: Review the generated worklist before applying changes in an ESP, and route suppression leakage or over-benchmark bounce and complaint trends through the appropriate audit gate. <br>
Risk: Memory writes can persist hygiene reports and worklists beyond the immediate session. <br>
Mitigation: Write memory only after explicit user permission and avoid persisting unnecessary subscriber-level details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/list-hygiene-monitor) <br>
- [Publisher profile](https://clawhub.ai/user/aaron-he-zhu) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Recurring List-Hygiene Checklist](references/hygiene-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with cohort tables, trend reads, worklist buckets, handoff summary, and optional shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs recommendations and worklists for user review; it does not safely execute email account changes itself.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
