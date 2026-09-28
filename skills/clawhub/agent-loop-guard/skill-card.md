## Description:

Helps developers identify excessive steps and repeated actions in agent traces, then suggests when to stop a looping run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0 (release metadata); MIT (Python code per LICENSE.md); all rights reserved (documentation and theory)

## Use Case:

Developers and engineers use this skill to check agent action traces for excessive steps or repeated behavior and receive a loop-risk assessment and stopping advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trace files may contain sensitive action details.

Mitigation: Run the helper only on trace files you intend it to read; do not include credentials or sensitive plaintext.

Risk: The helper reports loop risk but does not automatically stop a running agent.

Mitigation: Review its diagnosis and enforce stopping limits in the agent runtime separately.

Risk: Release license metadata differs from the bundled terms, which distinguish code from documentation and theory.

Mitigation: Review the bundled licensing notes and confirm rights for each component before reuse or redistribution.

## Reference(s):

- [Agent Loop Guard on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-loop-guard)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports trace step count, loop risk, stopping advice, and a brief diagnosis; does not itself stop an agent.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; bundled SKILL.md says 1.1.0 and manifest.json says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
