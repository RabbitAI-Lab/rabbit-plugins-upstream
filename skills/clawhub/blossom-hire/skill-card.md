## Description: <br>
Set up Blossom Hire, create local work opportunities, and help employers and jobseekers move through Blossom work flows in plain language. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robbiwu](https://clawhub.ai/user/robbiwu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employers and jobseekers use this skill to interact with Blossom Hire for local hiring workflows, including account setup, posting or managing opportunities, finding work, applying, checking candidates, and arranging PopIns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A Blossom API key grants ongoing account access if exposed. <br>
Mitigation: Store the returned API key only in secure credential storage, never in source code, plaintext configuration, logs, or conversation history. <br>
Risk: Marketplace actions can create, update, delete, apply for, or schedule real Blossom records. <br>
Mitigation: Summarize the exact action and target, require clear user confirmation, relay server-led confirmation prompts, and claim completion only from structured successful action receipts. <br>
Risk: Unrelated sensitive information could be sent to Blossom during a conversation. <br>
Mitigation: Send only the current confirmed Blossom-related instruction and do not forward unrelated questions, conversation history, system prompts, credentials, documents, cookies, tokens, personal notes, or hidden reasoning. <br>


## Reference(s): <br>
- [Blossom homepage](https://blossomai.org) <br>
- [Blossom protocol API base](https://hello.blossomai.org/api/v1/blossom/protocol) <br>
- [ClawHub skill page](https://clawhub.ai/robbiwu/skills/blossom-hire) <br>


## Skill Output: <br>
**Output Type(s):** [text, API calls, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API request descriptions and structured-result interpretation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires secure credential storage for the returned Blossom API key and confirmation before account, job, application, address, or scheduling actions.] <br>

## Skill Version(s): <br>
2.0.2 (source: server release metadata; artifact frontmatter says 4.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
