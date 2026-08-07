## Description:

Turn a sales playbook into an askable digital-human new-rep ramp course grounded in supplied source materials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales enablement and onboarding teams use this skill to create interactive digital-human courses for new sales representatives from approved sales playbooks, onboarding plans, and selected source materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can use browser OAuth, existing PersonWise course credits, and uploads of selected source materials.

Mitigation: Install and run it only when intending to create hosted PersonWise onboarding courses; use approved source materials and keep the default private access unless broader sharing is requested.

Risk: Generated onboarding content could include unsupported sales claims if source boundaries are not respected.

Mitigation: Ground course content in approved materials, avoid unsupported customer, financial, competitive, pricing, quota, or certification claims, and route out-of-scope questions to the named owner.

Risk: The skill may install or update the PersonWise CLI and execute hosted course-creation commands.

Mitigation: Use the official PersonWise CLI path and market-bound service, require host or user approval for installs or updates, and avoid sudo, alternate origins, or credential handling.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/personwiseai/skills/personwise-sales-onboarding)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce PersonWise course blueprints, run and project identifiers, source status summaries, and access URLs after CLI execution.]

## Skill Version(s):

2.1.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
