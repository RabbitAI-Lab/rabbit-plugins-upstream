## Description: <br>
Audits installed agent-skill packages for cleanup decisions using usage, overlap, burden, risk, and optional ablation or community evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent-workspace maintainers use this skill to audit installed agent skills, identify low-value or overlapping packages, and produce conservative manual-review recommendations with optional Markdown or JSON evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read local skill directories and optional usage, history, ablation, or community files supplied by the user. <br>
Mitigation: Use explicit --skills-root and output paths, and avoid passing sensitive transcript exports unless they are required for the audit. <br>
Risk: Cleanup recommendations could be mistaken for permission to remove or disable skills automatically. <br>
Mitigation: Treat delete, merge-delete, quarantine, and similar outcomes as human-review recommendations before taking action. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/gongyu0918-debug/skills/skill-usefulness-audit) <br>
- [Skill homepage](https://github.com/gongyu0918-debug/skill-usefulness-audit) <br>
- [Scoring rubric](references/scoring-rubric.md) <br>
- [Ablation protocol](references/ablation-protocol.md) <br>
- [Report narration prompt](references/report-narration-prompt.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Natural-language report with optional Markdown evidence, JSON audit evidence, and ablation plan files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Recommendations are manual-review guidance; the skill does not automatically delete, merge, quarantine, isolate, or disable skills.] <br>

## Skill Version(s): <br>
0.3.17 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
