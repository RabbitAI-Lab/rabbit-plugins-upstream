## Description:

Helps users adapt popular SkillScan-style workflows into practical plans, checklists, and artifacts for fixing bugs, hardening setup, improving reliability, and creating related skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

AI-agent users, skill authors, maintainers, and teams use this helper to turn a concrete workflow request into a plan, checklist, implementation artifact, and verification note. It provides planning guidance rather than a validated security scan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may cause unrelated requests to select this workflow helper.

Mitigation: Prefer explicit invocation or narrower activation settings.

Risk: The workflow's demand score and planning guidance do not establish that a skill is secure.

Mitigation: Treat this as workflow guidance, not a validated security scanner, and review and scan skills before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-skillscan-security-workflow-helper)
- [Requirement plan](references/requirement-plan.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Checklists, Plans, Artifacts]

**Output Format:** [Text or Markdown tailored to the requested deliverable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Practical and adapted to the user's context; includes a verification note when appropriate and favors local-hardware-friendly approaches.]

## Skill Version(s):

0.20261021.131013 (source: server-resolved release version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
