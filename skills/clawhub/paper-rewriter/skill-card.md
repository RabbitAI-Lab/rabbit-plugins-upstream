## Description:

Helps scholars review and revise Chinese or English academic prose for clarity and natural style while checking that key facts and terminology survive edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Scholars, editors and research teams use this skill to identify repetitive or stiff academic phrasing, revise drafts in Chinese or English, and check that numbers, citations and protected terminology remain intact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Draft manuscripts may contain sensitive information and are read from user-specified paths.

Mitigation: Use only files and output locations you are authorized to access; review locally written reports before sharing.

Risk: Style scores and revision suggestions can be mistaken for proof of AI authorship or change academic meaning.

Mitigation: Treat scores as writing prompts, review every edit, and use integrity checks to preserve numbers, citations and terminology.

Risk: Editing assistance may be misused to obscure authorship or required AI-use disclosures.

Mitigation: Use it for legitimate quality editing and follow applicable institutional and journal disclosure rules.

Risk: Experimental PDF extraction can produce incomplete or garbled text; learned term guards persist locally.

Mitigation: Inspect extracted text or use UTF-8 text input, and review saved term guards before subsequent scans.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/paper-rewriter)
- [English style guide](references/style_guide_en.md)
- [Chinese style guide](references/style_guide_zh.md)
- [Academic integrity and disclosure guidance](references/compliance.md)
- [Worked examples](references/examples.md)
- [API reference](references/api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, HTML, CSV, Guidance]

**Output Format:** [Revised prose and review guidance in text or Markdown; optional JSON, HTML and CSV reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Style scores are heuristic self-checks, not authorship determinations; integrity checks flag changes to protected facts and terms.]

## Skill Version(s):

2.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
