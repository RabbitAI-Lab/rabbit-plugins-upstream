## Description:

Converts common length, weight, temperature, speed, storage, area, and volume units with local-only calculations and Chinese or English unit names.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonyhuya](https://clawhub.ai/user/tonyhuya)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and end users use this skill to run quick local unit conversions from a shell. It is suited for routine conversions across supported measurement categories without network access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install metadata may install python3 if it is missing.

Mitigation: Review and approve package installation before deploying in managed environments.

Risk: The skill returns unit conversions from its supported local tables and aliases.

Mitigation: Check critical or regulated calculations against an authoritative source before relying on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonyhuya/skills/unit-converter)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Plain text conversion output with Markdown command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local execution; python3 may be installed if missing.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
