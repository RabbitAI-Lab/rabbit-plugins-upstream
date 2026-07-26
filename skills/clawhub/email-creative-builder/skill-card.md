## Description: <br>
Email Creative Builder drafts a single email creative with subject-line variants, a preheader, body copy, one CTA, a plain-text alternate, and message-match notes tied to approved claims. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing teams and agents use this skill to draft or iterate one email creative for promotional, cold-outbound, or newsletter workflows while keeping destination message-match and claims review visible. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Email drafts may include claims, offers, or personalization that are not approved for the audience, jurisdiction, or offer window. <br>
Mitigation: Verify claims, disclosures, destination message-match, and compliance details before use; keep unresolved items visibly flagged instead of treating the draft as ready to send. <br>
Risk: The skill can use marketing context such as landing pages, claims records, campaign exports, and consent or suppression information. <br>
Mitigation: Treat exported or scraped inputs as untrusted, and verify recipient consent and suppression status outside the draft before any send decision. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/email-creative-builder) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Email Creative Modes](references/email-creative-modes.md) <br>
- [Subject Line Specs](references/subject-line-specs.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown email creative with subject-line variants, preheader, body copy, CTA, plain-text alternate, message-match notes, and handoff summary.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Drafting support only; sending requires separate approval and consent/suppression checks.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
