## Description:

Find what the owner knows about a person or a project across Telegram, MAX, mail and notes through memo, and record facts, memories and key documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to search the owner's selected messaging, mail and notes for information about a person or project, including prior agreements, then record useful facts, memories or key documents for the owner's review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation may lead to private-message or email searches for ordinary questions about people or projects.

Mitigation: Restrict activation to requests about stored communications or notes, select relevant accounts explicitly, and use read-only mode when searching is sufficient.

Risk: The external npm package implementation was not verified in this review.

Mitigation: Review the package before installation; disable agent decisions when the owner should approve every project finding.

## Reference(s):

- [Cli Memo on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-memo)
- [WireCat publisher profile](https://clawhub.ai/user/wirecat)
- [@wirecat/cli-memo on npm](https://www.npmjs.com/package/@wirecat/cli-memo)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Text or Markdown answers with cited stored references; commands may return JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search coverage can be bounded or incomplete; recorded findings remain pending owner review.]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
