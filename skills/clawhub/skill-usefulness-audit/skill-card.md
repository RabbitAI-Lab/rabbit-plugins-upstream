## Description: <br>
Review your installed agent skills to see what you actually use, what overlaps, and what may no longer be worth keeping. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to audit installed skills for actual usage, overlap, maintenance burden, cleanup candidates, and optional ablation evidence. It supports manual review workflows by producing short reports, Markdown evidence, JSON evidence, or ablation plans from local skill directories and user-provided usage files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The audit can read local skill directories and user-provided usage or history files that may contain sensitive conversations, paths, project names, or customer data. <br>
Mitigation: Provide the narrowest relevant skill roots and evidence files, and avoid broad transcript exports unless they are needed for the review. <br>
Risk: Cleanup recommendations could be mistaken for automatic deletion or disabling instructions. <br>
Mitigation: Treat deletion, merge-delete, quarantine, and cleanup outputs as manual-review recommendations and review the generated evidence before changing installed skills. <br>


## Reference(s): <br>
- [Skill homepage](https://github.com/gongyu0918-debug/skill-usefulness-audit) <br>
- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/skill-usefulness-audit) <br>
- [Scoring Rubric](references/scoring-rubric.md) <br>
- [Ablation Protocol](references/ablation-protocol.md) <br>
- [Report Delivery Contract](references/report-narration-prompt.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Natural-language report, Markdown evidence, JSON evidence, and optional ablation-plan JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local report, evidence, JSON, or ablation-plan files when requested by command options.] <br>

## Skill Version(s): <br>
0.3.18 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
