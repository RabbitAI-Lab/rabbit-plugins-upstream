## Description: <br>
Audit LLM evaluation or benchmark repositories for integrity and credibility practices across seven dimensions, producing a scored report with file:line evidence, severity, and concrete fixes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[conorbronsdon](https://clawhub.ai/user/conorbronsdon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, benchmark maintainers, and reviewers use this skill to audit an LLM evaluation or benchmark repo before publishing numbers, submitting to a grant or conference, or relying on a leaderboard. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill inspects the target benchmark repository and may use GitHub CLI to query open pull requests when configured. <br>
Mitigation: Run it only against the intended benchmark repo, understand the active GitHub CLI authentication context, and treat PR lookups as read-only audit support. <br>
Risk: The audit can recommend methodology or leaderboard changes that affect published benchmark claims. <br>
Mitigation: Review findings before applying fixes, and have benchmark maintainers approve any edits, reruns, or publishing changes separately. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/conorbronsdon/skills/eval-integrity) <br>
- [eval-integrity canonical home](https://github.com/conorbronsdon/eval-integrity) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [Dimension audit briefs](artifact/patterns/dimension-prompts.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown scored audit report with file:line evidence, severity labels, and concrete fixes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only audit output; the skill reports findings and proposes fixes but does not edit the target benchmark.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
