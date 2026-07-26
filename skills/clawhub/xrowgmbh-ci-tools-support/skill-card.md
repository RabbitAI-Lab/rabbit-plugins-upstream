## Description: <br>
Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and support maintainers use this skill to triage eligible CI Tools support issues and discussion threads, answer from public documentation or provided context, and hand off unsafe or out-of-scope requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Support may be provided to an unintended requester if SUPPORT_TRUSTED_DOMAINS is stale or too broad. <br>
Mitigation: Keep SUPPORT_TRUSTED_DOMAINS current and verify the requester domain before answering. <br>
Risk: Private customer details, private URLs, private logs, or internal project names could be exposed in public support replies. <br>
Mitigation: Mark issues confidential when they include sensitive details and do not quote private logs into public places. <br>
Risk: Incorrect CI Tools guidance could be given if component behavior or inputs are assumed. <br>
Mitigation: Inspect the relevant public component template, documentation, issue, merge request, or pipeline log before answering. <br>


## Reference(s): <br>
- [ci-tools-support Support on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown support replies with citations or concise handoff guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses are constrained to eligible CI Tools support requests and public or explicitly provided information.] <br>

## Skill Version(s): <br>
4.165.2 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
