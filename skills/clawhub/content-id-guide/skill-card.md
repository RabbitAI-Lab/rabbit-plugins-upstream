## Description:

Guides creators, managers, and labels through automated copyright claim workflows and organizes their existing claim documentation into evidence summaries and deadline timelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[otherpowers](https://clawhub.ai/user/otherpowers)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, artists, managers, and label teams use this skill to understand automated content claims, distinguish claim types, collect their existing documentation, and map platform-specific deadlines without receiving legal advice or outcome predictions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive claim notices and creator documentation that may contain personal, account, financial, or rights-holder information.

Mitigation: Use recap or memory features only for information the user is comfortable storing, redact incidental third-party personal data from pasted notices, and keep the evidence organizer under the user's control.

Risk: Incorrect platform deadlines, windows, or money handling could mislead a creator during a time-sensitive claim process.

Mitigation: Use current official platform sources, include units for all windows, ask users to double-check live dashboards before acting, and avoid invented dates, amounts, or outcome predictions.

Risk: Formal legal steps such as counter notifications can require professional judgment.

Mitigation: Frame the skill as procedural information and document organization, not legal advice, and recommend a qualified professional at legal-weight moments.

Risk: Maintenance eval scripts may transmit transcripts or test material to external model APIs if run with real data.

Mitigation: Do not run live evals with real transcripts unless consent and privacy controls are in place.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/otherpowers/skills/content-id-guide)
- [Creative Traditions](references/creative-traditions.md)
- [Eval Plan](references/eval-plan.md)
- [Eval Seeds](references/eval-seeds.md)
- [Freshness Log](references/freshness-log.md)
- [Geography](references/geography.md)
- [Glossary](references/glossary.md)
- [Label Operators](references/label-operators.md)
- [Legal Help](references/legal-help.md)
- [Official Source Pairings](references/links.md)
- [Monetization Programs](references/monetization-programs.md)
- [Meta Rights Manager Reference](references/platform-meta.md)
- [TikTok Copyright Reference](references/platform-tiktok.md)
- [YouTube Content ID Reference](references/platform-youtube.md)
- [Extraction Red-Team Set](references/red-team-extraction.md)
- [Severity System](references/severity-badges.md)
- [Trigger Evals](references/trigger-evals.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Files, Shell commands]

**Output Format:** [Plain-language text and Markdown evidence organizers, with optional CSV/HTML templates and maintenance shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should cite current official platform sources, avoid legal advice, avoid outcome predictions, and preserve user-controlled records.]

## Skill Version(s):

1.0.4 (source: server release evidence and SKILL.md status)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
