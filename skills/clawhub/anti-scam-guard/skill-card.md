## Description: <br>
Checks URLs from LINE, SMS, email, or chat messages against phishing blocklists and heuristic rules to warn users about scam, fraud, or suspicious websites. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[phishguard-niki](https://clawhub.ai/user/phishguard-niki) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to check suspicious links before clicking or entering sensitive information. The skill can proactively scan URLs in messages and produce risk guidance in Traditional Chinese or English. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Safe results may be incomplete because the checker relies on blocklist data, heuristics, and allowlists. <br>
Mitigation: Treat low-risk output as advisory and continue standard phishing precautions before entering credentials, payment data, or other sensitive information. <br>
Risk: The skill runs python3 and fetches public blocklist shard files from GitHub while storing a local cache. <br>
Mitigation: Install only in environments where python3 execution, curl availability, GitHub access, and local cache storage are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/phishguard-niki/skills/anti-scam-guard) <br>
- [Phishguard source code link advertised by the skill](https://github.com/phishguard-niki/Phishguard) <br>
- [Public blocklist shard endpoint used by the checker](https://raw.githubusercontent.com/phishguard-niki/blocklist-data/main) <br>
- [Chrome Web Store extension](https://chromewebstore.google.com/detail/phishguard-scam-phishing-checker/odbipahjojmphhmjgicnafkhiikjandb) <br>
- [LINE Bot](https://line.me/R/ti/p/@163hfjhz) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, JSON, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown response based on JSON risk assessment from a local Python checker] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include per-URL risk level, matched source, reasons, and safety guidance; defaults to Traditional Chinese and matches English when the user writes in English.] <br>

## Skill Version(s): <br>
0.4.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
