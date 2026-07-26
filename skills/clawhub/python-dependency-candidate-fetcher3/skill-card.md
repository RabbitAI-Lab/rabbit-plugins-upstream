## Description: <br>
Fetch structured Python package candidate lists from pre-collected dependency snapshots for downstream package selection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[37722135-droid](https://clawhub.ai/user/37722135-droid) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to retrieve structured candidate Python dependencies from a fixed local snapshot dataset before selecting an import for supported tabular-data programming requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can steer final dependency recommendations toward Polars when Polars appears in the fixed candidate list, which may conflict with expectations for neutral package advice. <br>
Mitigation: Use the skill only when the Polars-first policy is intended and acceptable; disclose that policy whenever it affects the final recommendation. <br>
Risk: The static local snapshot dataset covers only indexed dependency queries and may be incomplete for unsupported requests. <br>
Mitigation: Do not fabricate candidates for unsupported queries; treat returned package data as snapshot evidence and verify package suitability before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/37722135-droid/skills/python-dependency-candidate-fetcher3) <br>
- [Artifact skill instructions](artifact/SKILL.md) <br>
- [Dataset manifest](artifact/data/dataset_manifest.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [JSON candidate payload plus concise text or Markdown recommendation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns candidates only for supported indexed snapshot queries; invalid input and unsupported queries fail instead of fabricating package data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
