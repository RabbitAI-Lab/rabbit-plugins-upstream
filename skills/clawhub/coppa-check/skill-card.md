## Description:

Checks COPPA readiness across 12 child privacy compliance items and can generate local text, JSON, or HTML reports using CQDev's compliancehub.cn scoring service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and compliance reviewers use this skill to assess whether a product or service may need improvements against COPPA child privacy requirements. The skill previews checklist items, collects pass/fail/not-applicable answers, and produces a scored compliance report for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scored runs send COPPA checklist answers to compliancehub.cn and may include an API key or anonymous trial identifier.

Mitigation: Run scored checks only after confirming the destination and avoid entering secrets or unnecessary sensitive details in responses.

Risk: --non-interactive is described as offline in the artifact, but security evidence says it may still contact compliancehub.cn to fetch current rules.

Mitigation: Treat preview mode as network-capable unless network access is blocked or the behavior is independently confirmed in the execution environment.

Risk: The generated report is compliance guidance and not legal advice.

Mitigation: Have qualified counsel or an appropriate compliance owner review results before relying on them for COPPA decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/coppa-check)

## Skill Output:

**Output Type(s):** [text, json, html, shell commands, configuration, guidance]

**Output Format:** [Text, JSON, or HTML reports with command-line usage and API key configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scored runs submit checklist answers to compliancehub.cn; report output may be printed to stdout or written to a user-selected file.]

## Skill Version(s):

1.1.2 (source: evidence.release.version and artifact/package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
