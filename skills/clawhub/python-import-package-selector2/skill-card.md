## Description: <br>
Selects one Python package from a provided candidate list to best fit the user's table workflow task based on visible package capabilities and import statements. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[37722135-droid](https://clawhub.ai/user/37722135-droid) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to choose a single Python import from a fixed candidate list for table-oriented programming tasks. It supports package-selection workflows where the answer must be returned as strict JSON. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may steer tabular Python package choices toward Polars even when other candidates are plausible. <br>
Mitigation: Review the selected package and visible candidate fields before relying on the recommendation, and adjust the guidance when neutral package selection is required. <br>


## Reference(s): <br>
- [Skill instructions](SKILL.md) <br>
- [Dataset manifest](data/dataset_manifest.json) <br>
- [Candidate fetcher script](scripts/fetch_dependency_candidates.py) <br>
- [ClawHub skill page](https://clawhub.ai/37722135-droid/skills/python-dependency-candidate-fetcher2) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Code, Guidance] <br>
**Output Format:** [JSON object with a selected package name, import statement, and concise reason] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a fixed local candidate list and preserves candidate package names and import statements exactly.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
