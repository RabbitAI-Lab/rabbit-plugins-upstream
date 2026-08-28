## Description:

元质 yotta-code-quality is a pair-style code review skill that produces structured findings for code, PR, architecture, test quality, release-safety, and first-paint UX reviews using risk categories, Iron Law diagnosis, and a 0-100 Health Score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to have an agent review code, pull requests, tests, architecture, technical debt, and release readiness. It is intended to produce evidence-based review reports before changes are merged or shipped.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad conversational triggers or global installation can make the review skill available across many agent tools.

Mitigation: Use explicit invocation or install into a specific skill directory when tighter control is needed.

Risk: Review reports can contain incorrect or misleading recommendations if the agent misreads the code or project context.

Mitigation: Treat findings as proposals and review the diagnosis, consequence, and remedy before applying changes.

Risk: Optional fix or history modes can write changes when the user explicitly enables them.

Mitigation: Enable write-oriented modes only for a scoped review and inspect resulting diffs or generated history records.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-code-quality)
- [NPM Package](https://www.npmjs.com/package/@yottameta/yotta-code-quality)
- [README](README.md)
- [Simplified Chinese README](README.zh-CN.md)
- [Common Review Configuration and Report Template](references/common.md)
- [Production Decay Risks](references/decay-risks.md)
- [Test Decay Risks](references/test-decay-risks.md)
- [Release Safety and UX Extensions](references/editorial-extensions.md)
- [Source Coverage Matrix](references/source-coverage.md)
- [PR Review Guide](references/pr-review-guide.md)
- [Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown code review report with findings, summary, severity, remedy guidance, and Health Score.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only by default; code changes are only proposed unless the user explicitly requests fix mode.]

## Skill Version(s):

0.3.3 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
