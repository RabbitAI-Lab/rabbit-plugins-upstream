## Description:

Turn image briefs into production-ready GPT Image 2.5 Studio jobs with exact-text manifests, reference-image role contracts, ratio and resolution choices, controlled edit rounds, and visual QA.

This skill is ready for commercial/non-commercial use.

## Publisher:

[julianreed888](https://clawhub.ai/user/julianreed888)

### License/Terms of Use:

MIT-0

## Use Case:

Creative producers, designers, marketers, and agents use this skill to convert image briefs into reviewed GPTImage-2-5.com Studio jobs for posters, packaging, ecommerce assets, UI mockups, storyboards, localized creatives, and precise image edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user may upload unintended or unauthorized assets to a third-party Studio.

Mitigation: Show the selected files before upload and obtain confirmation unless the current instruction already authorizes those exact inputs.

Risk: Generation may spend credits or consume quota.

Mitigation: Review the displayed credit cost, final prompt, and settings before starting generation.

Risk: Generated exact text may contain character-level errors, especially for critical legal, medical, financial, or safety copy.

Mitigation: Check text character-for-character at delivery size and recommend a deterministic layout tool when critical copy remains wrong.

Risk: Unsupported API, account, or automation assumptions could mislead users.

Mitigation: Use only the visible web Studio controls and do not invent endpoints, SDKs, authentication methods, or bypass flows.

## Reference(s):

- [Production contracts](references/production-contracts.md)
- [GPT Image 2.5 product capabilities and examples](https://gptimage-2-5.com/)
- [GPT Image 2.5 Studio](https://gptimage-2-5.com/studio)
- [ClawHub skill release](https://clawhub.ai/julianreed888/skills/gpt-image-2-5-production-studio)
- [ClawHub publisher profile](https://clawhub.ai/user/julianreed888)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, files]

**Output Format:** [Markdown job card, prompt text, acceptance-check results, edit ledger, execution summary, and selected image file reference when generation is completed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user review of selected files, final prompt, settings, and displayed cost before uploads or credit-consuming generation.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
