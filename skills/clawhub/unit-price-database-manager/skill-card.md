## Description: <br>
Manage construction unit price databases: update prices, track vendors, apply location factors, maintain historical records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Construction estimators, cost engineers, and project teams use this skill to maintain unit price records, compare vendor quotes, apply location and escalation adjustments, and produce price lookups or database status summaries for estimating and bidding workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read or write construction price database CSV files through filesystem access. <br>
Mitigation: Use explicit project paths, keep backups, and avoid granting access outside the intended pricing workspace. <br>
Risk: Bulk escalation, import, or export operations can change estimating records or expose proprietary vendor pricing. <br>
Mitigation: Review bulk operations before applying them, test changes on copies, and confirm export destinations before sharing files. <br>
Risk: Incorrect or stale pricing could affect estimates, bids, and cost-control decisions. <br>
Mitigation: Verify price dates, sources, location factors, and stale-price flags before relying on outputs for commercial decisions. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown with structured price summaries and optional Python or bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference CSV import/export workflows and should show last update dates, stale-price flags, sources, and validation issues when relevant.] <br>

## Skill Version(s): <br>
2.0.0 (source: artifact/claw.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
