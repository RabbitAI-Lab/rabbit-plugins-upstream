## Description: <br>
Audits paid advertising accounts using a typed 20-item ROAS profile to assess incremental contribution, wasted spend, measurement integrity, and gate outcomes before scaling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing operators, growth teams, and agent users use this skill to review paid-media exports, own-data outcome evidence, attribution windows, conversion lag, currency, and business constraints before launch or scale decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Advertising performance exports and business outcome data may contain sensitive commercial information. <br>
Mitigation: Install and run the skill only where the agent is permitted to process those exports, and provide only the account, outcome, attribution, and constraint data needed for the audit. <br>
Risk: Audit findings could be mistaken for permission to change spend, bids, audiences, or campaign state. <br>
Mitigation: Treat the output as analysis only; the artifact explicitly avoids campaign or budget changes and requires separate explicit approval before any account mutation. <br>
Risk: A standalone install may lack the deterministic scorer needed to produce a gate verdict. <br>
Mitigation: When the required runtime is unavailable, return NOT_SCORED with no gate verdict or persistent artifact, then rerun in a full plugin or repository install. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/ad-account-auditor) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/aaron-he-zhu) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Standalone Auditor Runtime](references/auditor-runtime.md) <br>
- [Distribution Manifest](distribution-manifest.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown audit report with structured status, verdict, score state, reconciliation tables, unknown evidence, and prioritized fixes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided account exports, own-data outcomes, currency/window/lag, and business constraints; does not mutate ad accounts.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
