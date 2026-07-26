## Description: <br>
Fetch structured shopping candidate lists from pre-collected shopping platform screenshot snapshots. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[37722135-droid](https://clawhub.ai/user/37722135-droid) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and shopping agents use this skill to retrieve a structured candidate pool from local shopping snapshot data before separate ranking, filtering, recommendation, or final selection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Static marketplace snapshots may be stale and do not prove current availability, price, or suitability. <br>
Mitigation: Downstream agents should verify current product details before recommending or buying anything. <br>
Risk: Some bundled snapshots may be poorly matched and capture dates may be missing. <br>
Mitigation: Check the matched query, source platform, and available snapshot provenance, and use the payload only as retrieval input rather than a final recommendation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/37722135-droid/skills/shopping-candidate-fetcher) <br>
- [SKILL.md](SKILL.md) <br>
- [Dataset manifest](data/dataset_manifest.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [JSON candidate-list payload with snapshot provenance fields, typically shown in Markdown with a shell command when invoked manually] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses static packaged snapshots; top_k defaults to 5 and must be greater than 0.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
