## Description:

Helps agents localize e-commerce listing assets for multiple regions with market-aware copy, size conversion tables, platform image specifications, and compliance-label reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketplace operators, and e-commerce content teams use this skill to turn one product asset set into localized listing guidance and generation commands for regions such as North America, Japan, Southeast Asia, and global marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected product images can be sent to cloud generation providers.

Mitigation: Use only approved providers and credentials, and do not submit confidential, regulated, or customer-identifying images unless organizational policy allows it.

Risk: Generated foreign-language text and compliance markings may be incorrect or unsuitable for publication.

Mitigation: Review localized text, size tables, and compliance-label suggestions with qualified reviewers before publishing listings.

Risk: Marketplace image rules and platform requirements can change.

Mitigation: Check the current official platform requirements and use updated rule overrides before relying on automated listing checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Provider CLI reference](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples, brand configuration inputs, validation output, and generated image-file paths when provider scripts are run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call cloud generation providers and may write localized listing images to user-specified output paths.]

## Skill Version(s):

1.0.9 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
