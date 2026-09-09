## Description:

Turns a topic brief, research materials, vendor case, policy event, or industry question into a publish-ready Markdown deep-dive article with source verification, originality review, planning gates, deterministic draft checks, review records, and evidence packaging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Content strategists, analysts, editors, and agent operators use this skill to turn a vetted topic brief and source corpus into a single technology-industry deep-dive article with fact tables, originality checks, planning approvals, draft review, revision, and final evidence packaging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner can copy detected secrets, private paths, customer data, or confidential company material into 05-machine-gate.json and the review package.

Mitigation: Redact sensitive drafts and source materials before scanning, treat scan reports as sensitive review artifacts, and avoid sharing the final package until credential and privacy findings are resolved.

Risk: A final validator pass alone may miss sensitive content or newly introduced draft issues.

Mitigation: Rerun the scanner on the final draft and review the machine-gate report before considering the article package complete.

Risk: Private writing profiles can contain personal, company, or style information that should not be copied into public artifacts.

Mitigation: Read only the needed profile fields at runtime, use a generic profile when no private profile is supplied, and keep full profiles outside the public skill package.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/industry-deep-dive-pipeline)
- [Planning Schema](references/planning-schema.md)
- [Evidence and Originality](references/evidence-and-originality.md)
- [Writing Profile Interface](references/writing-profile-interface.md)
- [Replay Evaluation](references/replay-evaluation.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown case bundle plus JSON machine-gate report and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stops at an approved article and evidence/review package; does not produce publication layouts, social copy, CMS drafts, or publishing actions.]

## Skill Version(s):

1.0.5 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
