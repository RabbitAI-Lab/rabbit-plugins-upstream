## Description: <br>
AI-driven settlement assistant for parsing natural-language payout rules, confirming rule interpretations, and processing local CSV or Excel data across equal-share, ranking, hybrid, and weighted settlement modes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luxieng030124-max](https://clawhub.ai/user/luxieng030124-max) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and operations teams use this skill to convert activity payout rules into settlement logic, confirm the rules before execution, and produce payout results from local CSV or Excel data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Payout accuracy issues could affect real settlements, especially weighted distribution results. <br>
Mitigation: Manually review settlement outputs, weighted distributions, and total-payout reconciliation before using results for real payouts. <br>
Risk: Broad triggers and under-declared file access may cause the skill to process local files more broadly than expected. <br>
Mitigation: Run the skill with only the intended input files available and review requested file access before deployment. <br>
Risk: A scoped uninstall command removes the local skill directory. <br>
Mitigation: Inspect destructive shell commands and confirm the target path before running uninstall steps. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/luxieng030124-max/skills/jiesuan) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact SKILL.md](artifact/SKILL.md) <br>
- [Artifact package metadata](artifact/package.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with Python configuration or code blocks and settlement result summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate local CSV settlement outputs when the agent executes the provided Python engine.] <br>

## Skill Version(s): <br>
2.1.3 (source: server release metadata; artifact package.json lists 2.1.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
