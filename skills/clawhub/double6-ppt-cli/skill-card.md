## Description:

Double6 PPT CLI helps agents create, fill, inspect, verify, and narrowly repair native editable PPTX decks from local content and PowerPoint templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[double6-ai](https://clawhub.ai/user/double6-ai)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and presentation-building agents use this skill to generate editable PowerPoint decks, fill existing PPTX templates, or run postflight checks and deterministic repairs while preserving source files and validation evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests local file access and PowerPoint automation authority for deck generation, verification, and repair workflows.

Mitigation: Install only after reviewing the bootstrap path, run it on copies of decks, and require explicit user authorization before installing or invoking OfficeCLI.

Risk: The security evidence reports unresolved dependency integrity concerns for Python locking, OfficeCLI package integrity, and the vendored BOM.

Mitigation: Ask the publisher for a working hashed Python lockfile, OfficeCLI package-lock or tarball integrity proof, and a corrected vendor BOM before using the skill on sensitive decks.

Risk: Vendored optional web, AI, or TTS material may be outside the intended PPTX workflow boundary.

Mitigation: Treat that material as out of scope unless the publisher removes or cleanly isolates it, and review package contents before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/double6-ai/skills/double6-ppt-cli)
- [OpenClaw homepage](https://github.com/double6-ai/double6-skills/tree/main/skills/double6-ppt-cli)
- [Authoring contract v0.2](references/authoring-contract.md)
- [Delivery gates v0.2](references/delivery-gates.md)
- [Machine contracts v2.0](references/machine-contracts.md)
- [Repair policy v0.2](references/repair-policy.md)
- [Adapter boundary](references/adapters.md)
- [Licenses and upstreams](references/licenses-and-upstreams.md)
- [PPT Master upstream](https://github.com/hugohe3/ppt-master)
- [OfficeCLI upstream](https://github.com/iOfficeAI/OfficeCLI)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples; generated workflow artifacts can include PPTX files, JSON receipts, and visual review outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full verification expects local Python, Microsoft PowerPoint automation, and explicitly authorized OfficeCLI 1.0.144 installation.]

## Skill Version(s):

0.2.1 (source: frontmatter, release metadata, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
