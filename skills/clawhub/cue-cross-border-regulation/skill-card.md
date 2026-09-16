## Description:

跨境法规调研 helps Chinese-speaking legal, compliance, and cross-border business teams research foreign regulations and produce source-linked Chinese Markdown reports with original clause identifiers and summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External legal, compliance, and business users use this skill to research non-China regulatory requirements for cross-border product launches, privacy, export controls, investment review, and employment questions. It is positioned for public-source legal research support, not as a substitute for formal legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Legal questions may include confidential business facts, disputes, client details, or regulated data that are sent to Cue.

Mitigation: Redact sensitive facts before use and avoid submitting regulated or client-identifying details unless the user has approved the data handling path.

Risk: The skill depends on a local Cue API key.

Mitigation: Store the key in a local secret store or configuration file with restrictive permissions, and never paste API keys into chat.

Risk: Generated Cue report links may expose research outputs if shared without understanding their access controls.

Mitigation: Review report contents before sharing links and limit distribution to recipients authorized to see the legal research.

Risk: The security summary flags forced service links and payment-referral messaging with limited user control.

Mitigation: Review outbound links and service/payment prompts before presenting final output in sensitive or customer-facing workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-cross-border-regulation)
- [Publisher profile](https://clawhub.ai/user/panting09266-ai)
- [Cue playbook](https://cuecue.cn/playbook)
- [Cue platform](https://cuecue.cn)
- [Cue API key management](https://cuecue.cn/api-key)
- [EUR-Lex](https://eur-lex.europa.eu)
- [United States Code](https://uscode.house.gov)
- [eCFR](https://www.ecfr.gov)
- [Singapore Statutes Online](https://sso.agc.gov.sg)
- [Congress.gov](https://www.congress.gov)
- [U.S. federal agencies directory](https://www.usa.gov/federal-agencies)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Chinese Markdown report with source links, Cue report URL when available, and local report path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key and may create a local report under ~/cue-reports/.]

## Skill Version(s):

1.0.7 (source: server release evidence and target metadata; artifact frontmatter reports 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
