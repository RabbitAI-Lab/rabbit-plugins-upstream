## Description:

Personal Legal Assistant helps users analyze legal questions, retrieve comparable cases and laws, draft or review legal documents, and compare rules across jurisdictions with source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, legal professionals, and agents use this skill to turn plain-language legal fact patterns into legal research, case comparisons, compensation calculations, source-linked analysis, and draft or reviewed legal documents. It is not a substitute for a licensed attorney for final decisions, filings, representation, or major rights-affecting actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles legal questions where incorrect or incomplete guidance could affect rights, filings, deadlines, or dispute strategy.

Mitigation: Use outputs as research and drafting assistance only; verify cited sources and consult a qualified lawyer before filing documents, signing agreements, waiving rights, or making major decisions.

Risk: Use may send legal facts, documents, and personal details to an external Cue service and stores an API key in local Cue configuration.

Mitigation: Share only necessary facts, redact unnecessary personal identifiers, protect the API key, and install the skill only when the publisher and service data handling are acceptable.

Risk: The security summary flags execution of code fetched from mutable external repositories.

Mitigation: Review and pin runner source before execution where possible, avoid automatic updates in sensitive environments, and run the workflow in a controlled workspace.

Risk: The skill can draft or review legal documents but does not provide representation, guarantee outcomes, or determine evidence authenticity.

Mitigation: Treat drafts as working material and require human legal review before submission or reliance.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/panting09266-ai/skills/cue-personal-legal-assistant)
- [Cue Platform](https://cuecue.cn)
- [Cue API Key Management](https://cuecue.cn/api-key)
- [Cue Skills Runner Repository](https://github.com/sensedeal/cue-skills)
- [Cue Skills Runner Gitee Mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown reports with source links, local report files, configuration guidance, and shell commands for running Cue research workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final reports should include the Cue original report link when a real conversation id is returned; legal conclusions require user verification and professional review for major matters.]

## Skill Version(s):

1.3.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
