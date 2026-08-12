## Description:

Zhanxing AOPT Skill runs fixed authorized-use diagnostic probes against an agent runtime and summarizes pass, block, or fail outcomes for reliability profiling.

This skill is for research and development only.

## Publisher:

[hixss](https://clawhub.ai/user/hixss)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and reliability researchers use this skill during authorized development and hardening work to profile how an agent runtime responds to a fixed diagnostic probe set. The results support regression checks, runtime comparisons, and evidence capture for behavior changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports a suspicious diagnostic tool with fixed high-risk probe strings in an opaque helper binary and local shell-wrapper execution despite claims that probe strings are not executed.

Mitigation: Install only for authorized adversarial agent-safety testing, review helper binary provenance before use, and treat all outputs strictly as test data.

Risk: The security guidance notes the inspected package is functionally inconsistent because the scheduler helper is not executable.

Mitigation: Verify packaging and executable permissions in a controlled environment before relying on diagnostic results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hixss/skills/zhanxing-aopt-skill)

## Skill Output:

**Output Type(s):** [Text, Shell commands]

**Output Format:** [Console text with diagnostic status lines and summarized counts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are reported per fixed check ID with pass, block, or fail status.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
