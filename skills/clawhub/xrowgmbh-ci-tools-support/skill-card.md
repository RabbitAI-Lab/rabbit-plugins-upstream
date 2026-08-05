## Description: <br>
Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support engineers, and maintainers use this skill to triage eligible GitLab support issues and discussions for the CI Tools components catalog, then provide grounded answers, focused follow-up questions, or handoffs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent could provide support to an ineligible requester or for an out-of-scope issue. <br>
Mitigation: Check the trusted requester domain list, confirm CI Tools relevance, and hand off or refuse when eligibility checks fail. <br>
Risk: Support replies could expose private customer details, private URLs, credentials, or private logs. <br>
Mitigation: Keep issues confidential when private details are present, avoid quoting private logs publicly, and scope any GitLab token to only the needed comment and label operations. <br>
Risk: The agent could give unsupported CI component behavior or unsafe access guidance. <br>
Mitigation: Inspect public component templates and cited sources before answering, ask for a public reproduction when context is missing, and refuse credential-recovery or access-bypass requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown support replies, focused follow-up questions, handoff or refusal notes, and triage label guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses should be grounded in public documentation, public repository content, public GitLab history, or details explicitly provided in the request.] <br>

## Skill Version(s): <br>
4.167.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
