## Description: <br>
Bid Collection helps agents monitor public tender and procurement sources, filter high-value opportunities by business track, and report prioritized leads while disclosing outbound requests, local writes, and scheduled monitoring side effects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cryptocxf](https://clawhub.ai/user/cryptocxf) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business development, sales operations, and procurement intelligence teams use this skill to scan public government, state-owned enterprise, industry, and aggregator tender sources for matching opportunities and generate prioritized lead reports. The skill can also run user-confirmed scheduled monitoring and local reporting. <br>

### Deployment Geography for Use: <br>
Global, with primary source coverage for Chinese public procurement and tender platforms. <br>

## Known Risks and Mitigations: <br>
Risk: Outbound requests may be sent to procurement platforms during scan, monitor, and add-source workflows. <br>
Mitigation: Review the target domain list before execution, use trusted public tender sources only, and cancel before requests are sent if the source set is unexpected. <br>
Risk: Monitor mode creates scheduled checks, sends notifications, and writes local logs. <br>
Mitigation: Enable monitor only after reviewing the scheduled-task side effects, keep default run limits unless persistence is required, and run monitor --stop when finished. <br>
Risk: Custom sources can expose search terms to unexpected hosts or trigger SSRF-like requests. <br>
Mitigation: Add only trusted public procurement URLs and reject localhost, private-network, metadata, or otherwise untrusted addresses. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cryptocxf/skills/bid-collection) <br>
- [Tender Lead Matching Rules & Priority Scoring](references/bid-matching-rules.md) <br>
- [Tender & Procurement Monitoring Source List](references/monitoring-sources.md) <br>
- [bid-collection Skill - Quick Start Guide](references/quick-start.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports and tables, JSON/HTML exports, logs, and command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results are written locally under leads-output/bid by default; monitor mode can create scheduled checks only after explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
