## Description:

BlazeMeter Service Virtualization helps agents inspect, list, retrieve, and update BlazeMeter service mock templates through an OOMOL-connected oo CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to operate BlazeMeter Service Virtualization from an agent session, including schema inspection, template retrieval, workspace listing, and confirmed JSON-safe updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands for the oo CLI, and the security scan recommends not allowing an agent to run them automatically.

Mitigation: Install or update the oo CLI only through a trusted, manually verified method before using the skill.

Risk: The update_service_mock_template action changes BlazeMeter Service Virtualization state.

Mitigation: Confirm the exact template, JSON payload, and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-blaze-meter-service-virtualization)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [BlazeMeter Service Virtualization](https://www.blazemeter.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON response handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions can run directly; write actions require user confirmation of the target payload and expected effect.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
