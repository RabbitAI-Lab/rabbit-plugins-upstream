## Description: <br>
Detects possible text trademark matches and infringement risk in e-commerce product titles and listing text across supported regions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
E-commerce sellers, marketplace operators, and listing reviewers use this skill to scan product titles, descriptions, bullet points, and keywords for registered trademark matches before publishing listings. It helps surface risk scores, matched trademarks, and blacklist or whitelist signals for human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product titles, listing text, session metadata, and the LinkFox API key are sent to the configured LinkFox gateway. <br>
Mitigation: Use the skill only with content appropriate to share with LinkFox, avoid personal data or confidential launches, and verify the configured gateway before use. <br>
Risk: Local response caching and saved JSON outputs may retain scanned listing text and trademark results. <br>
Mitigation: Inspect or disable caching where possible and clean saved LinkFox session data when the results should not persist. <br>
Risk: The onboarding flow may direct users to install a separate package from a URL. <br>
Mitigation: Allow onboarding package installation only after explicitly trusting the separate package and its source. <br>
Risk: The skill consumes paid LinkFox credits for API calls. <br>
Mitigation: Confirm user intent before repeated, broad, or high-frequency scans, especially when changing parameters would incur additional calls. <br>


## Reference(s): <br>
- [睿观-文本商标检测 API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-ruiguan-text-trademark-detection) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, json, shell commands, files] <br>
**Output Format:** [Markdown summaries and tables with JSON API responses saved to files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Small responses may be printed in full; larger responses are summarized while the full JSON is saved in the LinkFox session data directory.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
