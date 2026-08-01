## Description: <br>
Orchestrates multi-domain review (code, arch, tests, security) in a single pass. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to coordinate broad code, architecture, test, security, and release-readiness reviews and consolidate findings into a single action plan. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers can cause the review orchestration flow to activate for general review requests where a narrower review was intended. <br>
Mitigation: Install only when broad review orchestration is desired, or remove generic triggers before deployment. <br>
Risk: The skill can run a project-local deferred capture script automatically after action-plan synthesis. <br>
Mitigation: Change deferred capture to a confirm-before-run or dry-run step before using the skill in sensitive repositories. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-unified-review) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown review reports with action items, evidence appendices, and inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces consolidated review findings and prioritized remediation guidance from selected review domains.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
