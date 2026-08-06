## Description:

Read a liarjs fingerprint report and attribute each failing check to the component that produced it: launch configuration, page-modifying layer, network path, or machine image, while noting failures inherent to headless or datacenter environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liarjsdev](https://clawhub.ai/user/liarjsdev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to interpret low-scoring liarjs fingerprint reports, group failing check IDs by owning component, and distinguish actionable contradictions from expected headless or datacenter signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fingerprint reports can contain browser, network, and machine details that may be sensitive when shared outside the operating team.

Mitigation: Review and redact report contents before sharing them.

Risk: The skill may suggest npx-based liarjs commands to generate or compare scans.

Mitigation: Run package-based commands only from trusted sources and in an environment appropriate for browser fingerprint testing.

Risk: A fingerprint score reflects internal coherence, not whether a real site will accept or reject a browser.

Mitigation: Use the output as attribution guidance and avoid treating score improvements as outcome forecasts.

## Reference(s):

- [Interpreting a failing check](references/interpreting-checks.md)
- [liarjs CLI field notes](https://liarjs.dev/cli/)
- [ClawHub skill page](https://clawhub.ai/liarjsdev/skills/fingerprint-failure-triage)
- [Publisher profile](https://clawhub.ai/user/liarjsdev)

## Skill Output:

**Output Type(s):** [analysis, markdown, shell commands, guidance]

**Output Format:** [Markdown with grouped findings and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Interprets report data and may suggest one-change-at-a-time re-scan comparisons.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
