## Description: <br>
Runs NoxInfluencer creator and marketing-ops workflows through its CLI for creator discovery, due diligence, outreach operations, CRM and campaign work, monitoring, brand analysis, file workflows, and exports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[noxinfluencer](https://clawhub.ai/user/noxinfluencer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and marketing teams use this skill to find and evaluate creators, manage NoxInfluencer campaign and outreach operations, monitor creator or brand performance, and export selected results while keeping write actions behind preview and approval steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may save a NoxInfluencer API key locally during account setup. <br>
Mitigation: Use the documented device flow where possible, avoid passing API keys in argv or logs, and install the skill only when NoxInfluencer access is intended. <br>
Risk: API-backed creator search, lookalike, contact, export, and operational actions may consume NoxInfluencer quota or SaaS entitlements. <br>
Mitigation: Check quota and pricing before cost-sensitive work, use targeted page sizes, and review preview or dry-run output before executing charged or write actions. <br>
Risk: The skill can retrieve visible creator contact details and operate outreach workflows. <br>
Mitigation: Retrieve exported contact details only when explicitly requested, use platform email recipient flows for in-platform outreach, and require approval of recipients, sender, timing, and content before send or schedule actions. <br>
Risk: The skill can upload, download, create, update, or export NoxInfluencer files and business records. <br>
Mitigation: Use validate, preview, and dry-run stages where available; apply forced writes only after the user approves the exact object and action. <br>


## Reference(s): <br>
- [NoxInfluencer Skill Homepage](https://www.noxinfluencer.com/skills) <br>
- [Marketing Ops Workflows](artifact/references/marketing-ops.md) <br>
- [CLI Response Format](artifact/references/cli-response-format.md) <br>
- [Brand Monitor Workflows](artifact/references/brand-monitor.md) <br>
- [Platform Support](artifact/references/platform-support.md) <br>
- [Search Filter Semantics](artifact/references/search-filters.md) <br>
- [Verdict Heuristics Reference](artifact/references/verdict-heuristics.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Plain-language Markdown summaries with CLI-backed JSON results and local file outputs when exports or downloads are requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs the NoxInfluencer CLI, preserves returned IDs for follow-up actions, and reports output paths for generated export or report files.] <br>

## Skill Version(s): <br>
0.1.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
