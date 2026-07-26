## Description: <br>
A category-based memory skill that lets Claude store, retrieve, and delete categorized memories across chat sessions through a remote service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agent users and developers use this skill to save categorized memories with optional tags, retrieve memories by category or across all categories, and remove category-scoped or specific memories when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores and retrieves memory content through a remote service. <br>
Mitigation: Use only if you trust the remote memory service with the content being stored, and avoid storing sensitive material unless that trust decision is acceptable. <br>
Risk: The API key is saved locally in plaintext. <br>
Mitigation: Keep local file permissions restricted, rotate the key if exposure is suspected, and remove the saved key when it is no longer needed. <br>
Risk: Deletion tools can remove broad sets of memories, including category-wide deletion. <br>
Mitigation: Confirm the category and local/global scope before deletion, especially when using broad selectors such as all categories. <br>
Risk: The security summary says the documentation and safeguards do not clearly match the credential, remote storage, and deletion powers exposed by the skill. <br>
Mitigation: Review the skill before installing and use it only when the credential handling, remote storage behavior, and deletion semantics are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/alinklab/skills/remember-memory) <br>
- [XiaoBenYang service](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown or plain text summaries of remote API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided XBY_APIKEY; responses are derived from the remote service's raw data.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
