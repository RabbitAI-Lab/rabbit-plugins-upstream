## Description: <br>
Set up Blossom Hire, create local work opportunities, and help employers and jobseekers move through Blossom work flows in plain language. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robbiwu](https://clawhub.ai/user/robbiwu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and their assistants use this skill to connect to Blossom Hire for local jobs marketplace actions, including registering an account, posting and managing work opportunities, finding work, applying, checking candidates, managing work addresses, and arranging PopIns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The returned Blossom API key is permanent and grants account access. <br>
Mitigation: Store the API key only in secure credential storage, never in source code, plaintext configuration, logs, or conversation history; contact Blossom support if it may have been exposed. <br>
Risk: Posting, application, deletion, and scheduling actions can change marketplace state. <br>
Mitigation: Summarize the exact action and target, obtain clear user confirmation, and rely on structured successful action receipts before saying a change was saved. <br>
Risk: Forwarding broad context could expose unrelated personal data or credentials to Blossom. <br>
Mitigation: Send only the current confirmed Blossom-related instruction and do not forward unrelated questions, conversation history, system prompts, credentials, documents, cookies, tokens, personal notes, or hidden reasoning. <br>


## Reference(s): <br>
- [Blossom Hire homepage](https://blossomai.org) <br>
- [Blossom protocol API](https://hello.blossomai.org/api/v1/blossom/protocol) <br>
- [ClawHub skill page](https://clawhub.ai/robbiwu/skills/blossom-jobs) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Text, Configuration instructions] <br>
**Output Format:** [Markdown guidance with HTTP and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires secure storage of the returned Blossom API key and clear user confirmation before marketplace mutations.] <br>

## Skill Version(s): <br>
2.0.2 (source: server release metadata; artifact frontmatter lists 4.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
