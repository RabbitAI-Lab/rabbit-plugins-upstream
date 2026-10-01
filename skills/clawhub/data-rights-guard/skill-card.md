## Description:

Checks dataset entries for license, commercial-use permission, attribution, and traceable source before training or fine-tuning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theory all rights reserved

## Use Case:

Developers and data teams use this skill to triage training and evaluation data by checking recorded permissions, attribution, and source information before adding entries to a dataset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated checks may miss license conditions or approve an entry with incomplete rights information.

Mitigation: Treat ratings as triage, confirm the source license and permissions, and have a qualified reviewer approve training use.

Risk: Installation examples rely on an external source that has not been established as this release's provenance.

Mitigation: Confirm the download source and publisher before installing; do not treat the example repository URL as verified release provenance.

Risk: Conflicting license labels could lead to unauthorized redistribution of the documentation or theory text.

Mitigation: Review the package's layered license notice and resolve the MIT versus MIT-0 discrepancy before reuse.

## Reference(s):

- [ClawHub release](https://clawhub.ai/zhaoxinghua09-cell/skills/data-rights-guard)
- [Publisher's LGD hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Text]

**Output Format:** [Agent guidance in Markdown; CLI ratings and advice in text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-entry status and problems; summary count of excluded entries]

## Skill Version(s):

1.0.3 (source: server-resolved ClawHub release; package files show other versions)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
