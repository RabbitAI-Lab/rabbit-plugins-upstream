## Description: <br>
Share memories and state with other users by managing users, groups, permissions, subscriptions, and access control for an Ensue-backed memory knowledge base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[christinetyip](https://clawhub.ai/user/christinetyip) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, teams, and developers use this skill to share memory namespaces, create users and groups, grant or revoke access, and subscribe to memory changes through Ensue. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make lasting Ensue access-control changes, including deletes, revokes, org-wide grants, broad namespace patterns, and write or delete permissions. <br>
Mitigation: Require clear manual review before those operations, prefer narrow namespace patterns, and grant only the minimum action needed. <br>
Risk: The skill can reuse local Ensue credentials, and troubleshooting steps may expose the raw ENSUE_API_KEY. <br>
Mitigation: Set ENSUE_API_KEY explicitly for this skill and avoid commands that print or display the raw key. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/christinetyip/skills/shared-memory) <br>
- [Ensue Network](https://ensue-network.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON responses from the Ensue API] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ENSUE_API_KEY or a supported local Ensue credential source.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
