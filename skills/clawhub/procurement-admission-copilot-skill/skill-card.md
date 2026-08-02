## Description: <br>
Review-only copilot for B2B procurement admission that checks supplier material-package completeness and consistency, tracks approval-case status and gaps, and leaves admission decisions to human reviewers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement, supplier onboarding, and compliance reviewers use this skill to screen supplier qualification packages and approval-case queues for missing documents, identity conflicts, certificate expiry, inconsistent figures, stalls, and gaps before a human decision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may read an admission-ready or ready status as approval to admit a supplier. <br>
Mitigation: Treat readiness as a completeness and issue-status signal only, and keep final admission decisions in a separate human-owned review process. <br>
Risk: The skill requires access to procurement and supplier documents that may contain sensitive business information. <br>
Mitigation: Install and run it only in environments where the agent is permitted to access those documents, and limit inputs to the materials needed for the review. <br>


## Reference(s): <br>
- [Procurement Admission Qualification Checklist](references/qualification-checklist.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/procurement-admission-copilot-skill) <br>
- [Publisher Profile](https://clawhub.ai/user/haiyangchenbj) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Shell commands, Guidance] <br>
**Output Format:** [JSON readiness checks and Markdown material packages, readiness reports, or case dashboards] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Review-only outputs; deterministic checks provide the baseline and human reviewers keep final admission responsibility.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
