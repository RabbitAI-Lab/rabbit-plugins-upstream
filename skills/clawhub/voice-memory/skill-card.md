## Description: <br>
Voice Memory gives voice and phone agents persistent BlueColumn-backed memory for conversations, meetings, coaching sessions, sales calls, and journal entries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers building voice or phone agents use this skill to store call transcripts in BlueColumn and recall prior caller context before responding. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores and recalls caller conversations through a third-party service, which can create privacy and retention concerns for real caller, customer, meeting, coaching, sales, or journal data. <br>
Mitigation: Use it only where callers have appropriate notice or consent, BlueColumn retention and deletion policies are acceptable, and sensitive transcript content is minimized or redacted. <br>
Risk: Persistent voice memory can expose or mix context across people or accounts if memories are not separated carefully. <br>
Mitigation: Separate stored memories by caller or account before using recalled context in responses. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/voice-memory) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BlueColumn API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
