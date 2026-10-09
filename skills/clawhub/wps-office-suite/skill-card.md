## Description:

Automates the creation, editing, conversion, analysis, search, and redaction of office documents using available office software or Python tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams working with office documents use this skill to create and edit Word, Excel, and PowerPoint files, convert formats, and automate reporting and document workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scheduled tasks can persistently execute commands; the security assessment also reports a local command-injection bug.

Mitigation: Review scheduled commands before use, especially custom --cmd values, and avoid schedule --force unless the exact command is trusted.

Risk: Opening indexed files from untrusted or shared directories can expose the agent to unsafe document content.

Mitigation: Use doc-search --open only with trusted directories and review retrieved documents before acting on their contents.

Risk: Optional external AI or cloud services may receive confidential documents.

Mitigation: Keep confidential material local unless the selected endpoint and credentials are approved for that data.

Risk: Editing and converting documents can change files or lose complex formatting.

Mitigation: Back up important files and review converted or edited documents before distribution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/fyniujin/skills/wps-office-suite)
- [Usage and dependencies](README.md)
- [Architecture](ARCHITECTURE.md)
- [Official document formatting rules](references/gongwen_rules.yaml)

## Skill Output:

**Output Type(s):** [Files, Text, JSON, Guidance]

**Output Format:** [Office documents, PDF, text, and optional JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output formats and features depend on the available office engine and optional services.]

## Skill Version(s):

5.3.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
