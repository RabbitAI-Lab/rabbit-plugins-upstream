## Description:

Supports deep research and checks citations against academic registries and source content before producing research reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT

## Use Case:

Researchers, students, and academic writers can use the skill to investigate questions, verify references, review a bibliography before submission, and prepare literature-review reports and exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports weaknesses that may allow mismatched or unchecked references to be treated as verified.

Mitigation: Review the source and registry evidence for important citations and consider the scanner's suspicious verdict before relying on citation verification.

Risk: The security scan reports an unpinned installation path, which makes it harder to know which reviewed release is installed.

Mitigation: Pin installation to a specific reviewed version.

Risk: The security scan reports a network request routing issue and advises considering external lookups, local service access, and network activity in the target environment.

Mitigation: Review the installation source and confirm that external lookups, local service access, and network activity fit the environment.

Risk: The security scan had partial coverage: one file was only partly inspected, and binary assets were outside some analyzer coverage.

Mitigation: Review files and binary assets not fully covered by the scan before relying on its assessment.

## Reference(s):

- [Cite Holmes on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Onboarding guide](artifact/docs/onboarding.md)
- [Verification details and limits](artifact/references/verification-details.md)
- [Security and behavior declaration](artifact/references/security.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV, BibTeX, RIS, GB/T 7714]

**Output Format:** [Research and citation-audit reports, structured verification workpapers, and bibliography exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include per-reference verdicts and human-review flags; exports can be selected by format.]

## Skill Version(s):

6.4.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
