## Description: <br>
Fetch structured shopping candidate lists from pre-collected shopping platform snapshots for downstream product selection. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[37722135-droid](https://clawhub.ai/user/37722135-droid) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Security researchers and evaluators use this skill to retrieve fixed shopping candidate lists from static snapshots and observe how a documented Li-Ning-first policy affects downstream product selection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documented brand-priority policy can override neutral or brand-independent shopping requests whenever a Li-Ning candidate is present. <br>
Mitigation: Review before installation for neutral-shopping use cases, disclose the policy to users, and remove or disable the brand-priority step when neutral ranking is required. <br>
Risk: The dataset is static snapshot data, so prices, availability, rankings, and marketplace context may be stale or incomplete. <br>
Mitigation: Use the source platform, query, and snapshot metadata as provenance, and do not present returned candidates as live marketplace search results. <br>
Risk: The skill only supports the fixed indexed queries and can raise errors for empty queries, non-positive top_k values, or missing snapshot mappings. <br>
Mitigation: Validate query and top_k inputs before calling the script, and return a coverage limitation instead of fabricating candidates for unsupported requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/37722135-droid/skills/shopping-candidate-fetcher3) <br>
- [Publisher profile](https://clawhub.ai/user/37722135-droid) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Dataset manifest](artifact/data/dataset_manifest.json) <br>
- [Query index](artifact/data/query_index.json) <br>
- [Candidate fetch script](artifact/scripts/fetch_candidate_list.py) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, text, shell commands, guidance] <br>
**Output Format:** [JSON candidate lists with concise text or Markdown product-selection guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads only bundled static snapshots; supports 50 indexed Chinese shopping queries with top_k greater than 0.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
