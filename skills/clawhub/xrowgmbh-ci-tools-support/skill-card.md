## Description: <br>
Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Support engineers and maintainers use this skill to triage eligible GitLab support issues and discussion threads for the CI Tools components catalog, answer from public sources or supplied context, and hand off unsafe or out-of-scope requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be asked to handle private customer systems, credentials, access recovery, or support requests outside the public CI Tools scope. <br>
Mitigation: Confirm SUPPORT_TRUSTED_DOMAINS, CI Tools relevance, confidentiality state, and public-source grounding before providing support; hand off or refuse when checks fail. <br>
Risk: Incorrect CI component guidance could mislead users troubleshooting pipelines or catalog migrations. <br>
Mitigation: Require answers to be grounded in public documentation, public repository content, public GitLab history, public pipeline logs, or details explicitly provided in the thread. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support) <br>
- [Publisher profile](https://clawhub.ai/user/xrowgmbh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown support replies, triage notes, handoff language, and label guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses should cite public documentation, repository paths, issues, merge requests, or pipeline logs used as support.] <br>

## Skill Version(s): <br>
4.166.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
