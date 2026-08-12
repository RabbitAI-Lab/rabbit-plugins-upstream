## Description:

Read a liarjs fingerprint report and attribute each failing check to the component that produced it - what the check id measures, whether the signal comes from the launch configuration, the page-modifying layer, the network path or the machine image, and which failures are inherent to headless or datacenter environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liarjsdev](https://clawhub.ai/user/liarjsdev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to interpret low-scoring liarjs fingerprint reports, group failed checks by source, and distinguish inherent headless or datacenter signals from findings that need an owner.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fingerprint analysis can be dual-use when it informs browser automation tuning.

Mitigation: Use the skill for authorized measurement attribution and avoid turning findings into hidden bypass, exfiltration, persistence, or destructive actions.

Risk: A liarjs score can be mistaken for a prediction of how a specific site will treat a browser.

Mitigation: Report improvements as removed internal contradictions only, because site outcomes can also depend on IP reputation, account history, and behavior.

Risk: The skill may propose Bash commands to run liarjs scans or diffs.

Mitigation: Review commands before execution and run them only in environments where scanning the target browser setup is authorized.

## Reference(s):

- [Interpreting Checks](references/interpreting-checks.md)
- [liarjs CLI field notes](https://liarjs.dev/cli/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Interprets report data and groups findings by launch configuration, page-modifying layer, network path, and machine or image source.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
