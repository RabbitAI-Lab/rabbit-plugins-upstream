## Description: <br>
Manage and retrieve long-term memories with LanceDB using semantic vector search, category filtering, and detailed metadata storage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pntrivedy](https://clawhub.ai/user/pntrivedy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to add a local LanceDB-backed long-term memory store, then add, search, update, delete, and inspect memories with categories, tags, metadata, and importance scores. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill durably stores memory content and metadata on local disk, which can retain secrets or sensitive personal data if users save them. <br>
Mitigation: Avoid saving secrets or sensitive personal data unless local retention is intended and access to the storage directory is appropriately controlled. <br>
Risk: The artifact uses a hard-coded LanceDB storage path. <br>
Mitigation: Verify or change the storage path before use so data is written to the intended local location. <br>


## Reference(s): <br>
- [Lancedb Memory on ClawHub](https://clawhub.ai/pntrivedy/skills/lancedb-memory) <br>


## Skill Output: <br>
**Output Type(s):** [code, configuration, guidance] <br>
**Output Format:** [Python modules and concise usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores memory content and metadata in a local LanceDB database.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
