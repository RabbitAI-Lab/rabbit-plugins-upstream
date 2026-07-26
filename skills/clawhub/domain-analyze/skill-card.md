## Description: <br>
Domain Analyze produces evidence-classified reports about a domain's registration, DNS, safety, backlinks, cross-TLD footprint, website status, and market or legal context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abtdomain](https://clawhub.ai/user/abtdomain) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and domain operators use this skill to perform due diligence on a specific domain before technical investigation, acquisition research, or operational review. It emphasizes source attribution, observation dates, and Fact, Inference, or Unknown labels for material findings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Domain lookups and web searches may disclose queried domains to configured external providers. <br>
Mitigation: Use the skill only when that disclosure is acceptable for the domain under review, and rely on the configured providers' handling policies. <br>
Risk: Fetching a malicious, phishing, or malware-hosting domain could expose the analysis environment to unsafe content. <br>
Mitigation: Check safety results before fetching and do not fetch domains or variants flagged as malicious, phishing, or malware-hosting. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/abtdomain/skills/domain-analyze) <br>
- [Publisher Profile](https://clawhub.ai/user/abtdomain) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown report with sourced findings and evidence classifications] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full reports cover registration, DNS and email, website status, safety, backlinks, cross-TLD footprint, market and legal context, evidence gaps, and observation timestamps; narrow requests return only the relevant sections.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
