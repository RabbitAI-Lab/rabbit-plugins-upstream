## Description:

Grill-the-plan makes the agent pause before multi-step or risky work to break a plan into checkpoints, expose parameters and risks, and wait for explicit user approval before implementation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fbbyqsyea](https://clawhub.ai/user/fbbyqsyea)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill when they want an agent to scrutinize a proposed multi-step plan, confirm key decisions one node at a time, and stop when requirements or risk assumptions change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can slow down routine work or activate more often than a command-only skill.

Mitigation: Use it for multi-step, risky, or decision-heavy tasks where explicit confirmation is valuable.

Risk: The source skill is primarily written in Chinese, which may make the workflow less accessible to non-Chinese users.

Mitigation: Translate or adapt the prompts for the deployment audience before broad rollout.

## Reference(s):

- [Pre-Flight checklist example](artifact/references/example.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown planning checklist, risk summary, confirmation prompts, and progress notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable artifacts; content is conversational planning guidance.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
