## Description:

Analyzes Xiaohongshu account IDs to produce seven-dimension scoring diagnostics, optimization recommendations, similar-account benchmarks, and exportable HTML reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanyi-github](https://clawhub.ai/user/yuanyi-github)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, MCN operators, brand marketers, and competitive analysts use this skill to evaluate Xiaohongshu/REDnote accounts, compare account portfolios, and plan content optimization from RedFox account data and web research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses REDFOX_API_KEY and sends Xiaohongshu account IDs to RedFox services.

Mitigation: Use it only in trusted environments, keep the API key in an environment variable, and confirm the key can be reset or revoked.

Risk: Generated reports may contain sensitive account analysis and local HTML created from external data.

Mitigation: Treat report files as sensitive, avoid sharing them broadly, and avoid opening reports from untrusted data until HTML escaping is fixed.

Risk: Security evidence recommends a version that verifies TLS certificates and bundles or removes remote browser scripts.

Mitigation: Prefer an updated release with those transport and browser-script safeguards before broader deployment.

## Reference(s):

- [API Guide](references/api_guide.md)
- [Workflow Guide](references/workflow_guide.md)
- [Report Template](references/report_template.md)
- [Benchmark Data](references/benchmark_data.md)
- [RedFoxHub](https://redfox.hk?source=clawhub)
- [ClawHub Skill Page](https://clawhub.ai/yuanyi-github/skills/xiaohongshu-account-analyzer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown diagnostic reports, HTML report files, JSON data templates, and shell commands/configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports single-account and multi-account analysis; generated HTML report content is expected to match the conversational report.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
