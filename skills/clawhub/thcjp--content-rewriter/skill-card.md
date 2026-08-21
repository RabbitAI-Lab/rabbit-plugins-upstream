## Description:

Helps agents rewrite content for platform-specific style and run SimHash duplicate checks before publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Content operations teams and publishing agents use this skill to adapt a source text for different platform styles and check recent content fingerprints for same-platform duplicates or cross-platform similarity before release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LLM rewrite mode may send submitted content through the OpenClaw gateway to 9Router.

Mitigation: Use local rewrite mode for sensitive unpublished material unless external processing is acceptable.

Risk: Local detect mode keeps recent content fingerprints for duplicate checks.

Mitigation: Treat fingerprint history as local operational data and avoid using it with sensitive material unless local retention is acceptable.

Risk: Automated rewriting can change tone or meaning in ways that affect publication quality.

Mitigation: Review rewritten content before publishing, especially when warning or block results trigger a rewrite.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/content-rewriter)
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Rewrite results include original text, rewritten text, platform, and mode; detection results include pass, warning, or block status with SimHash distance details.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
