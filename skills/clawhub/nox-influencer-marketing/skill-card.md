## Description: <br>
Runs NoxInfluencer creator discovery and marketing-ops workflows through its CLI, covering influencer search, creator evaluation, outreach operations, campaign and CRM management, brand monitoring, and exports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[noxinfluencer](https://clawhub.ai/user/noxinfluencer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing teams and agents use this skill to discover and evaluate creators across YouTube, TikTok, and Instagram, operate NoxInfluencer outreach and campaign workflows, monitor brand and video performance, and export operational data after user-approved actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate a NoxInfluencer account and access marketing, creator-contact, CRM, brand-monitor, export, and download data. <br>
Mitigation: Install only when account-level operation is intended, review contact exports, email sends, CRM updates, brand-monitor unlocks, and downloads before approval, and apply organizational consent and retention rules. <br>
Risk: Write or unlock workflows can change NoxInfluencer state or consume quota and entitlements. <br>
Mitigation: Use documented dry-run, validate, and preview steps before execution, and apply force or send actions only after explicit approval of the exact object, recipients, timing, and content. <br>
Risk: Creator contact details may include personal data intended for controlled outreach or export workflows. <br>
Mitigation: Retrieve visible contact information only when explicitly requested for external use, limit the returned details to what is needed, and handle the data under the user's consent and retention obligations. <br>


## Reference(s): <br>
- [NoxInfluencer Skills](https://www.noxinfluencer.com/skills) <br>
- [ClawHub Skill Page](https://clawhub.ai/noxinfluencer/skills/nox-influencer-marketing) <br>
- [Brand Monitor Workflows](references/brand-monitor.md) <br>
- [CLI Response Format](references/cli-response-format.md) <br>
- [Marketing Ops Workflows](references/marketing-ops.md) <br>
- [Platform Support](references/platform-support.md) <br>
- [Search Filter Semantics](references/search-filters.md) <br>
- [Verdict Heuristics Reference](references/verdict-heuristics.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Plain-language Markdown summaries with CLI-backed JSON result interpretation and occasional file paths for exports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the noxinfluencer CLI and NoxInfluencer account access; write actions use dry-run, validation, preview, and explicit approval flows where supported.] <br>

## Skill Version(s): <br>
0.1.15 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
