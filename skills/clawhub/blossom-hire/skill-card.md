## Description: <br>
Set up Blossom Hire, create local work opportunities, and help employers and jobseekers move through Blossom work flows in plain language. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robbiwu](https://clawhub.ai/user/robbiwu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employers and jobseekers use this skill to set up Blossom Hire accounts, create or manage local work listings, search for opportunities, apply to roles, and review marketplace status through confirmed Blossom actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles personal details for account setup, addresses, job listings, applications, and related marketplace actions. <br>
Mitigation: Send only the minimum data needed for the confirmed Blossom action and avoid forwarding unrelated conversation history, prompts, documents, credentials, or secrets. <br>
Risk: The returned Blossom API key grants full account access until Blossom rotates or revokes it. <br>
Mitigation: Treat the API key as a secret, keep it only in runtime session memory, and contact Blossom support for rotation or revocation if exposure is suspected. <br>
Risk: Registration requires a user-chosen Blossom passKey. <br>
Mitigation: Ask the user to choose a unique passKey, use it only for the one-time registration call, and never reuse, echo, log, or send it to any other endpoint. <br>
Risk: Marketplace mutations can create, update, delete, post, or apply to records on behalf of the user. <br>
Mitigation: Summarize the intended action and wait for clear user confirmation before sending any mutating request. <br>


## Reference(s): <br>
- [Blossom Hire ClawHub listing](https://clawhub.ai/robbiwu/skills/blossom-hire) <br>
- [Publisher profile](https://clawhub.ai/user/robbiwu) <br>
- [Blossom homepage](https://blossomai.org) <br>
- [Blossom privacy policy](https://blossomai.org/privacypolicy.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API calls, Guidance] <br>
**Output Format:** [Plain-language responses with structured Blossom API requests and concise status updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation before creating, updating, deleting, posting, or applying to marketplace records.] <br>

## Skill Version(s): <br>
1.0.21 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
