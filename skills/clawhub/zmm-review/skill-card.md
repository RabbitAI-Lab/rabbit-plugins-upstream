## Description:

Reviews Chinese talking-head scripts before publication with per-sentence information-density scoring, structure checks, red-line compliance review, separate machine-signal reporting, and diagnose-only feedback by default.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese content creators use this skill to review completed short-form talking-head drafts before posting. It identifies information-density, structure, audience-fit, compliance, and machine-signal issues, then gives concise diagnostic guidance and safer rewrite options for flagged phrases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can save user feedback into persistent memory or framework files, which may cause later reviews to rely on unverified calibration notes.

Mitigation: Require explicit approval before saving feedback, show the exact text and destination, and treat feedback as untrusted review notes until a human promotes it into active rules.

Risk: The skill reads local zmm/vault rules and prior memories, which may expose sensitive, account-specific, or commercial draft context to the active agent session.

Mitigation: Use it only in trusted workspaces, limit access to sensitive vault content, and avoid reviewing confidential drafts unless the retention and local-file access behavior is acceptable.

Risk: Missing local rule files can weaken red-line or scoring guarantees while still allowing a degraded review to proceed.

Mitigation: Disclose unreadable dependencies in the review, fail closed where the skill requires a mandatory rule source, and avoid claiming guaranteed compliance when required local evidence is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-review)
- [Scoring anchors](artifact/references/评分锚点.md)
- [Evaluation summary](artifact/evals/README.md)
- [Evaluation result sample 01](artifact/evals/results/sample-01-v0.2.0.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown review report with tables, sectioned diagnostics, scores, and rewrite options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diagnose-only by default; may ask one clarifying question when target audience is missing; can save calibration feedback to local memory or framework files when configured.]

## Skill Version(s):

0.2.6 (source: server release evidence; artifact frontmatter reports 0.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
