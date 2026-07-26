## Description: <br>
AstrMap VOC helps ecommerce sellers collect Amazon reviews and analyze customer feedback, frequent product issues, improvement ideas, and review trends. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sparkbayes](https://clawhub.ai/user/sparkbayes) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External ecommerce sellers and their agents use this skill to create or query AstrMap Amazon review-analysis tasks, retrieve VOC insights, inspect negative and positive review patterns, and produce product-improvement guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The AstrMap API key is sent to api.astrmap.com for authentication. <br>
Mitigation: Use a limited or read-only API key when possible, pass it through CUSTOMER_INSIGHTS_API_KEY, and rotate or disable it when no longer needed. <br>
Risk: Creating collection or analysis tasks can require the AstrMap desktop client and an Amazon buyer account. <br>
Mitigation: Use a dedicated buyer account rather than a primary seller or business account, and keep it separate from production Amazon credentials. <br>
Risk: Desktop client downloads add supply-chain and local-installation risk. <br>
Mitigation: Download only from AstrMap's official site, verify HTTPS, check published file integrity, and confirm code signing where available. <br>
Risk: Automatic analysis and incremental collection can consume AstrMap account credits. <br>
Mitigation: Check the point balance and obtain user confirmation before creating tasks, running automatic analysis, or starting incremental collection. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sparkbayes/skills/astrmap-voc) <br>
- [AstrMap API Reference](references/api_reference.md) <br>
- [AstrMap Security Guide](references/security.md) <br>
- [AstrMap API](https://api.astrmap.com) <br>
- [AstrMap Website](https://www.astrmap.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CUSTOMER_INSIGHTS_API_KEY and may call api.astrmap.com for requested AstrMap review tasks.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
