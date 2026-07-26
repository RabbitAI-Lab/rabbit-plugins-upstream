## Description: <br>
Scans websites for GDPR/DSGVO compliance from the terminal, without requiring an API key for quick scans, and reports a 0-100 score plus findings about trackers, cookies, consent banners, pre-consent tracking, fonts, and third-party transfers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[2g4y1](https://clawhub.ai/user/2g4y1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and site owners use this skill to run quick website compliance checks and summarize GDPR/DSGVO indicators such as cookies, trackers, consent banners, external fonts, and security-related findings. The result is an automated technical indication, not legal advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Website URLs provided for scans are sent to compliancescan.eu for analysis. <br>
Mitigation: Use the skill only for URLs that may be shared with that service, and avoid scanning sensitive internal targets. <br>
Risk: Authenticated full scans require COMPLIANCESCAN_API_KEY and may consume credits. <br>
Mitigation: Configure the API key only when full scans or account features are intended, never expose the key, and confirm before scans that may consume credits. <br>
Risk: Compliance scan results are automated technical indicators and may be incomplete or cached. <br>
Mitigation: Report only fields returned by the API, include scan scope and cache notes, and avoid presenting results as legal advice. <br>


## Reference(s): <br>
- [Compliancescan homepage](https://compliancescan.eu) <br>
- [Compliancescan ClawHub skill page](https://clawhub.ai/2g4y1/skills/compliancescan) <br>
- [Publisher profile](https://clawhub.ai/user/2g4y1) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Concise Markdown with compliance score, scan scope, findings, risk flags, cache notes, and failure guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Quick scans send user-provided website URLs to compliancescan.eu and may use an optional API key for authenticated full scans.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
