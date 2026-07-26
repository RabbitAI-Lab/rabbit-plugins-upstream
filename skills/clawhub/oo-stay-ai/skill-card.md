## Description: <br>
Stay AI lets an agent query account settings, subscriptions, and orders through the OOMOL stay_ai connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and operators use this skill to have an agent read Stay AI account, subscription, and order information through an OOMOL-connected account. It is intended for lookup, filtering, and pagination workflows rather than direct API handling by the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can query Stay AI account, subscription, and order data through the user's connected OOMOL account. <br>
Mitigation: Install only when that read access is acceptable, and review requested filters or identifiers before running commands that expose customer or order details. <br>
Risk: Future connector actions may include write or destructive operations even though this version lists read-oriented actions. <br>
Mitigation: Confirm the exact action and payload with the user before any action tagged write or destructive, and rely on the live connector schema before sending data. <br>


## Reference(s): <br>
- [Stay AI homepage](https://stay.ai) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Skill page](https://clawhub.ai/oomol/skills/oo-stay-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Bash commands and JSON payloads; connector responses are JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads and treats current untagged actions as read-oriented.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
