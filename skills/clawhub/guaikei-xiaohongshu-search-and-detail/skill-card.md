## Description:

Retrieves public Xiaohongshu search results, note details, comments, and creator posts as structured JSON through GUAIKEI API-backed command-line workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content, marketing, and research teams use this skill to collect public Xiaohongshu data for trend discovery, competitor monitoring, KOL screening, comment analysis, and downstream reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the GUAIKEI API token and Xiaohongshu keywords, note links, profile links, and retrieved results to a third-party service.

Mitigation: Install only where that data sharing is authorized, store GUAIKEI_API_TOKEN securely, and avoid submitting sensitive or private targets.

Risk: The skill saves retrieved results locally under logs/ by default.

Mitigation: Review local log retention and access controls, and clear generated logs when results should not persist.

Risk: The top-level summary understates that the skill supports search, note detail retrieval, profile post collection, and comment analysis.

Mitigation: Review the full capability set and apply internal use policies before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xiaohongshu-search-and-detail)
- [GUAIKEI service website](https://www.guaikei.com)
- [完整参数说明](references/options.md)
- [技能更新日志](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON]

**Output Format:** [JSON results with concise command and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and may write retrieved results to local logs.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; source package reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
