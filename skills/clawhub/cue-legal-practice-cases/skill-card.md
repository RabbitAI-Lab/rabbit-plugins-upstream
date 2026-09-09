## Description:

疑难法律实操案例库 helps agents research Chinese legal practice questions by retrieving public judgments, regulatory Q&A, practical cases, disputed issues, comparable outcomes, and source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, lawyers, and legal practitioners use this skill to compare public Chinese judgments, arbitration decisions, regulatory materials, and practice cases for civil, criminal, labor, lending, divorce, inheritance, traffic accident, and defense questions. The resulting report supports case triage, disputed-issue analysis, comparable-case research, litigation strategy, and evidence planning, but does not replace professional legal advice.

### Deployment Geography for Use:

Global, with content focused on public legal and regulatory materials from China.

## Known Risks and Mitigations:

Risk: Sensitive legal facts may be sent to cuecue.cn during research.

Mitigation: Redact names, ID numbers, phone numbers, addresses, case numbers, employer or client details, and other confidential facts before use.

Risk: The skill asks users to run an unpinned external Python runner.

Mitigation: Review the runner before installing or executing it, and only run a version whose source and integrity you can verify.

Risk: The Cue API key may be stored in ~/.cue/config.json.

Mitigation: Restrict ~/.cue/config.json permissions to owner-only and rotate the key if it may have been exposed.

Risk: The generated report may be incomplete or unsuitable as legal advice.

Mitigation: Review cited case numbers and source links, account for non-public materials and jurisdictional limits, and consult a qualified legal professional for decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-legal-practice-cases)
- [Publisher profile](https://clawhub.ai/user/panting09266-ai)
- [Cue platform](https://cuecue.cn)
- [Cue API key](https://cuecue.cn/hub/api-key)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [China Judgments Online](https://wenshu.court.gov.cn)
- [China Securities Regulatory Commission](https://www.csrc.gov.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown report with case lists, disputed-issue summaries, court-rule comparisons, action guidance, risk notes, case numbers, source links, and optional shell commands for setup or conversion]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are written to a local Markdown file path and may be converted to Word or PDF with pandoc when the user installs the required dependencies.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
