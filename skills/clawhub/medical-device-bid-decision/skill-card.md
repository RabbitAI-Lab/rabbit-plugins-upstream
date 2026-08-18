## Description:

Assists users in evaluating medical-device, consumables, reagent, and hospital IT procurement bids by analyzing buyer history, incumbent suppliers, likely competitors, pricing benchmarks, configuration signals, and bid risk from Zhiliaobiaoxun tender data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and bidding teams use this skill to decide whether to pursue a specific hospital procurement opportunity, estimate pricing, and understand buyer and competitor signals. The skill is intended for public tender-data analysis and decision support, not as a substitute for independent commercial or legal judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts zhiliaobiaoxun.com services and uses or creates a ZLBX API key.

Mitigation: Install only when that service dependency is acceptable, and prefer preconfiguring a user-owned ZLBX_API_KEY before use.

Risk: Credentials may be stored locally under ~/.zlbx/config.json.

Mitigation: Protect the local configuration file and avoid sharing logs, screenshots, or reports that could expose credential-related details.

Risk: Automatic registration uses device-derived attributes for trial-account de-duplication.

Mitigation: Review the registration prompt before consenting, or preconfigure ZLBX_API_KEY to skip automatic registration.

Risk: Generated reports may preserve signed detail links returned by the service.

Mitigation: Check generated HTML reports and links before forwarding them outside the intended audience.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/medical-device-bid-decision)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [API quick reference](artifact/references/api-quick.md)
- [Auto-registration workflow](artifact/references/auto-register.md)
- [Bid-decision workflow](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [HTML report renderer](artifact/scripts/render_report.py)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown bid-decision report with optional locally saved HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source citations, signed detail links returned by the service, and local absolute paths to generated HTML reports.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
