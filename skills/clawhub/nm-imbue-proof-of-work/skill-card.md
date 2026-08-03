## Description: <br>
Enforces validation and evidence collection before an agent claims implementation work, pull requests, or review deliverables are complete. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill as a pre-completion gate to require reproduced failures, tested fixes, acceptance criteria, and evidence logs before implementation work, pull requests, or deliverables are claimed ready. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Evidence logs may expose tokens, account IDs, internal hostnames, or sensitive local paths if copied into shared deliverables. <br>
Mitigation: Redact sensitive values before sharing evidence and avoid logging credentials or private infrastructure details unless explicitly required. <br>
Risk: Validation examples include network and authentication-status checks that may be unnecessary for a given task. <br>
Mitigation: Confirm that each network or auth check is needed, prefer read-only commands, and limit validation to the current task scope. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-proof-of-work) <br>
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>
- [Acceptance Criteria module](modules/acceptance-criteria.md) <br>
- [Evidence Logging module](modules/evidence-logging.md) <br>
- [Validation Protocols module](modules/validation-protocols.md) <br>
- [Output Contracts module](modules/output-contracts.md) <br>
- [Atlassian Definition of Done guidance](https://www.atlassian.com/agile/project-management/definition-of-done) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with checklists, command examples, evidence logs, and output contract snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompts agents to capture reproducible command output, citations, timestamps, acceptance criteria, and blocker status.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
