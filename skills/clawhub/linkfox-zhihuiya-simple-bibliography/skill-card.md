## Description: <br>
Retrieves simple bibliographic metadata for a single patent from the Zhihuiya patent database by patent ID or publication number. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and patent/IP practitioners use this skill to retrieve front-page patent metadata for a specific patent identifier, including title, abstract, applicants, inventors, dates, classifications, and citation references. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent identifiers and related session metadata are sent to LinkFox/Zhihuiya during lookup. <br>
Mitigation: Use the skill only when the user explicitly chooses this provider and accepts sending the patent lookup details to the service. <br>
Risk: Full lookup responses are persisted on local disk, which may retain patent metadata beyond the immediate conversation. <br>
Mitigation: Review the saved response location and apply local retention, access-control, or cleanup practices appropriate for the workspace. <br>
Risk: Lookups consume LinkFox API credits and the skill warns that multiple patent checks can be costly. <br>
Mitigation: Confirm before running lookups, especially for multiple patents, and keep the one-patent-per-call behavior. <br>
Risk: The skill includes automatic feedback reporting behavior. <br>
Mitigation: Require confirmation before submitting feedback so user statements and task context are not reported unexpectedly. <br>


## Reference(s): <br>
- [Zhihuiya Simple Bibliography API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-simple-bibliography) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance, Files] <br>
**Output Format:** [Markdown summaries and JSON API responses saved to local files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single-patent lookup; full responses are persisted locally and large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
