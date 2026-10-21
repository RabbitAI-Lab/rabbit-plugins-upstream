## Description:

Analyzes one Douyin, Xiaohongshu, TikTok, or YouTube post into its hook, structure, title formula, call to action, and reusable content template, with source-checked quotations and platform engagement data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and researchers use this skill to study a single social-media post's hook, pacing, and engagement, then develop an original content outline. It does not predict reach or assess an entire account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provided links or share text are sent to LinkDigest; text results are cached by link and may be available to others requesting the same link.

Mitigation: Submit only public content; do not provide private links or sensitive share text.

Risk: Exposing the LinkDigest API key in chat or source code could permit unauthorized use.

Mitigation: Keep the key in an environment variable or protected skill configuration; never paste it into chat or commit it.

Risk: The optional npx MCP bridge runs an additional package.

Mitigation: Prefer the bundled Python or curl workflow; verify or pin the MCP package before using it.

Risk: A breakdown can omit inaccessible content or include approximate timings and imperfect transcription.

Mitigation: Review missing-content notes and source quotations, and treat structural analysis as guidance rather than a performance guarantee.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/jackchew7143/skills/linkdigest-viral-breakdown)
- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest OpenAPI specification](https://linkdigest.dev/openapi.json)

## Skill Output:

**Output Type(s):** [Analysis, Text, Guidance]

**Output Format:** [Markdown or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-post breakdown with approximate time markers or image numbers, checked quotations, an engagement snapshot, reusable templates, and notes on missing content; optional translation.]

## Skill Version(s):

1.2.0 (source: server-resolved release metadata; artifact frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
