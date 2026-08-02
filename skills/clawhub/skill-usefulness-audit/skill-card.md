## Description: <br>
Review your installed agent skills to see what you actually use, what overlaps, and what may no longer be worth keeping. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to audit installed agent skills, compare usage and overlap, identify low-confidence cleanup candidates, and prepare evidence-backed ablation plans without automatically removing skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installed skill folders and user-provided usage or history files may contain sensitive conversations, local paths, project names, or customer data. <br>
Mitigation: Provide only intended evidence files, keep generated reports local unless reviewed, and avoid sharing raw JSON or full Markdown evidence unless needed. <br>
Risk: Delete, merge-delete, quarantine, or cleanup labels could be mistaken for automatic removal instructions. <br>
Mitigation: Treat cleanup labels as manual-review recommendations and confirm evidence before changing or removing any installed skill. <br>
Risk: Structure-only audits have lower-confidence usefulness and cleanup recommendations. <br>
Mitigation: Prefer direct usage logs, history fallback evidence, ablation results, or community metrics before making cleanup decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/skill-usefulness-audit) <br>
- [Project homepage](https://github.com/gongyu0918-debug/skill-usefulness-audit) <br>
- [Ablation protocol](references/ablation-protocol.md) <br>
- [Report narration prompt](references/report-narration-prompt.md) <br>
- [Scoring rubric](references/scoring-rubric.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Natural-language report with optional Markdown report, JSON evidence, and ablation plan files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include manual-review cleanup recommendations, score evidence, risk notes, and ablation planning details.] <br>

## Skill Version(s): <br>
0.3.20 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
