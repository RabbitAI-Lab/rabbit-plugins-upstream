## Description:

AI Content Discloser generates bilingual explicit AI-content disclosure statements, suggested implicit metadata labels, and platform placement tips for full, assisted, or mixed AI-created content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, creators, and compliance reviewers use this skill to draft disclosure text and metadata suggestions for AI-involved content before publication. It is a governance aid and does not replace legal or professional review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install instructions use a mutable global installation path.

Mitigation: Use a pinned commit or audited local copy before deployment.

Risk: Generated disclosure text can state that content was human-reviewed without confirming that review occurred.

Mitigation: Remove or revise the human-reviewed claim unless a real human review has happened.

Risk: Disclosure wording may become stale against China and EU requirements.

Mitigation: Verify legal wording against current official requirements before publishing regulated content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-content-discloser)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Plain text or JSON disclosure content, with agent-facing guidance suitable for Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic zero-dependency CLI output; generated human-review claims require user verification.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and release changelog text report 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
