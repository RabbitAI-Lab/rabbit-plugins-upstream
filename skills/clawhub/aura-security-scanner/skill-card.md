## Description: <br>
Scan AI agent skills for malware, credential theft, prompt injection, and dangerous permissions before installing them <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aurasecurity-creator](https://clawhub.ai/user/aurasecurity-creator) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and security-minded agent users use this skill to submit skill URLs to AURA's scanner before installation and review verdicts, risk scores, findings, and recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scanned skill URLs are sent to AURA or to the endpoint configured through AURA_API_URL. <br>
Mitigation: Avoid submitting private repository links, token-bearing URLs, presigned links, or internal service URLs unless that endpoint is trusted. <br>
Risk: Scan verdicts are advisory and may miss issues or report false positives. <br>
Mitigation: Review findings and recommendations before installing or deploying a scanned skill. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/aurasecurity-creator/skills/aura-security-scanner) <br>
- [AURA Security website](https://aurasecurity.io) <br>
- [AURA Security GitHub repository](https://github.com/aurasecurityio/aura-security) <br>
- [AURA Security API scan endpoint](https://api.aurasecurity.io/scan-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown text containing a scan verdict, risk score, findings, recommendations, and error guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns one response per supplied skill URL; scan requests use the configured AURA_API_URL endpoint with a 30 second timeout.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
