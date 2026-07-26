## Description: <br>
OKKI Go is a B2B prospecting engine for AI agents and sales teams. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okki-op](https://clawhub.ai/user/okki-op) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales teams, operators, and agent users use this skill to search global B2B prospect companies, unlock selected company details and contact emails, draft or send outbound email, and check delivery status or credit balance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run installers and optional update reminder scripts. <br>
Mitigation: Review installer and notification behavior before installation, and decline update notifications unless they are needed. <br>
Risk: The skill can save API keys locally. <br>
Mitigation: Use platform secret storage where possible and avoid printing, logging, or storing API keys outside approved secure paths. <br>
Risk: Prospect, contact, unlock, and email workflows can retain sensitive data on disk. <br>
Mitigation: Periodically delete OKKI Go temporary and artifact files that contain contacts, raw prospect records, or message content. <br>
Risk: Paid unlocks and email sends can consume credits or EDM quota. <br>
Mitigation: Require explicit user confirmation before every paid unlock or email send. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/okki-op/skills/okki-go) <br>
- [Publisher profile](https://clawhub.ai/user/okki-op) <br>
- [OKKI Go homepage](https://go.okki.ai) <br>
- [OKKI Go pricing](https://go.okki.ai/pricing) <br>
- [API reference](references/api-reference.md) <br>
- [Authentication and API key setup](references/authentication.md) <br>
- [Context firewall](references/context-firewall.md) <br>
- [Output contracts](references/output-contracts.md) <br>
- [Paid actions](references/paid-actions.md) <br>
- [Search fast path](references/search-fast-path.md) <br>
- [Search strategy](references/search-strategy.md) <br>
- [Script README](scripts/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with compact script-rendered tables, summaries, status rows, file paths, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local raw or detail files for prospect, contact, unlock, and email workflows; compact output hides raw identifiers and email bodies unless explicitly requested.] <br>

## Skill Version(s): <br>
1.3.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
