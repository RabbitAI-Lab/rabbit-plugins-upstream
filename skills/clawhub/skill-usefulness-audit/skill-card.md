## Description: <br>
Review your installed agent skills to see what you actually use, what overlaps, and what may no longer be worth keeping. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT No Attribution <br>


## Use Case: <br>
Developers and agent administrators use this skill to audit installed agent skills for actual usage, functional overlap, outcome impact, runtime burden, and cleanup recommendations before making manual retention decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: History and usage files may contain sensitive conversations, local paths, project names, or customer data. <br>
Mitigation: Pass explicit --skills-root paths and provide history or usage files only when comfortable with local scanning. <br>
Risk: Cleanup recommendations could be mistaken for authorization to remove, merge, quarantine, isolate, or disable skills. <br>
Mitigation: Treat those recommendations as manual-review prompts and do not change installed skills automatically. <br>


## Reference(s): <br>
- [Scoring Rubric](references/scoring-rubric.md) <br>
- [Ablation Protocol](references/ablation-protocol.md) <br>
- [Report Delivery Contract](references/report-narration-prompt.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/skill-usefulness-audit) <br>
- [Project Homepage](https://github.com/gongyu0918-debug/skill-usefulness-audit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Natural-language report with optional Markdown evidence, JSON evidence, and ablation-plan files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include local audit recommendations; deletion, merge, quarantine, or disable actions require manual review.] <br>

## Skill Version(s): <br>
0.3.19 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
