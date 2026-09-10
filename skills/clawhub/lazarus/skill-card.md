## Description:

Lazarus v2 helps agents discover evidence-backed dead-domain candidates or recover archived pages for rewrite-source notes, private corpora, or gated republishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsorgcn](https://clawhub.ai/user/adsorgcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use lazarus to research dead domains, verify they are not live, grade archived pages by heuristic index evidence, and package recoverable material with privacy and copyright review gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can recover or package archived website material that may still be protected by copyright or trademark rights.

Mitigation: Use the default rewrite-source mode when possible, require explicit acknowledgment before public republishing, and stop public deploy output when the review gate fails.

Risk: Recovered archives can contain PII, secrets, internal endpoints, or sensitive URL components.

Mitigation: Keep PII scanning enabled, fail the gate on secrets, redact findings, and avoid sending unsanitized URLs or sensitive queries to third-party providers.

Risk: Death and index status can be misclassified if a live site, parked page, redirect, or blocked service is treated too casually.

Mitigation: Run target validation, DNS and HTTP checks, redirect validation, Wayback evidence collection, and heuristic index grading before recovery; ask the user on uncertain verdicts and stop on live sites.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/adsorgcn/skills/lazarus)
- [I-Lang homepage](https://ilang.ai)
- [AutoCode](https://github.com/ilang-ai/autocode)
- [OpenClaw Skills](https://github.com/ilang-ai/ilang-openclaw)
- [Archive.org account signup](https://archive.org/account/signup)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, JSONL, Configuration, Guidance]

**Output Format:** [Markdown, JSON, JSONL, YAML frontmatter, and plain text bundle files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recovery Bundle outputs can include candidates.json, death_report.json, url_index.jsonl, graded_urls.jsonl, review_report.json, CONTENT_INDEX.md, source notes, optional raw snapshots, and deploy-notes.md when the gate passes.]

## Skill Version(s):

2.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
