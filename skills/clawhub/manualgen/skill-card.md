## Description:

ManualGen helps agents generate detailed user operation manuals for large software projects through staged extraction, knowledge graph construction, validation, and incremental refinement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songzhou666](https://clawhub.ai/user/songzhou666)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical writers, and operations teams use ManualGen to turn complex application workspaces into detailed, evidence-backed user operation manuals with step-by-step workflows, permissions matrices, and cross-module process coverage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can scan a project workspace and create or modify many documentation and state files automatically.

Mitigation: Run it only in intended workspaces, review generated directories and manuals before sharing, and keep generated state out of version control when it may expose sensitive project structure.

Risk: Generated manuals and evidence indexes may contain sensitive implementation details or project-specific data.

Mitigation: Use the bundled verification and technical-leak scans, apply the privacy notice's redaction rules, and perform human review before publication.

Risk: Reset operations with knowledge-base purging can remove generated analysis artifacts.

Mitigation: Use reset and purge options only when restarting intentionally and after preserving any artifacts that must be retained.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/songzhou666/skills/manualgen)
- [Server-resolved GitHub Repository](https://github.com/songzhou666/ManualGen)
- [README](artifact/README.md)
- [Privacy Notice](artifact/privacy/privacy-notice.md)
- [Deep FAQ](artifact/references/faq-deep.md)
- [Anti-Patterns](artifact/references/anti-patterns.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown manuals, JSON state artifacts, and concise command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated manuals and state files may include project structure and evidence indexes; review outputs before sharing.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata; internal skill frontmatter reports 6.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
