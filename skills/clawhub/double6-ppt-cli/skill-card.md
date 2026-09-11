## Description:

Double6 PPT CLI helps agents create, fill templates for, inspect, verify, and narrowly repair native editable PPTX decks using ppt-master and OfficeCLI-based workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[double6-ai](https://clawhub.ai/user/double6-ai)

### License/Terms of Use:

Apache License 2.0

## Use Case:

Developers and agents use this skill to generate presentations from Markdown, text, structured materials, and authorized local images, to reuse existing PPTX templates, and to run PPTX quality checks with bounded repairs. It is not intended for PDF or DOCX parsing, web image search, image-only slides, HTML slides, text-to-speech, or video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional bootstrap path can run unverified npm install scripts for OfficeCLI.

Mitigation: Review the bootstrap path before installation, use a constrained environment, and verify the OfficeCLI package source and integrity where possible.

Risk: The skill reads and writes local PPTX copies and may automate PowerPoint or LibreOffice during verification.

Mitigation: Run it only on decks and directories intended for the workflow, keep original files separate, and review generated evidence before relying on repaired outputs.

Risk: Important operational and safety boundaries are documented primarily in Chinese.

Mitigation: Non-Chinese readers should translate the documentation before installation or production use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/double6-ai/skills/double6-ppt-cli)
- [Double6 PPT CLI Homepage](https://github.com/double6-ai/double6-skills/tree/main/skills/double6-ppt-cli)
- [ppt-master](https://github.com/hugohe3/ppt-master)
- [OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)
- [Adapter boundary](references/adapters.md)
- [Authoring contract v0.2](references/authoring-contract.md)
- [Delivery gates v0.2](references/delivery-gates.md)
- [Licenses and upstreams](references/licenses-and-upstreams.md)
- [Machine contracts v2.0](references/machine-contracts.md)
- [Repair policy v0.2](references/repair-policy.md)
- [Verification tiers and test report](references/test-report-and-verification-tiers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON receipts, and local PPTX run artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create run directories, copied PPTX outputs, package diffs, inspection maps, render manifests, and verification evidence.]

## Skill Version(s):

0.3.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
