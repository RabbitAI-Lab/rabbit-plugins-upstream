## Description: <br>
Wire a Fieldy webhook transform into Moltbot hooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mrzilvis](https://clawhub.ai/user/mrzilvis) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to connect Fieldy voice transcripts to Moltbot Gateway webhooks, trigger an agent when a wake word is present, and keep non-triggering transcripts as local JSONL records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Raw Fieldy transcript text may be stored in plaintext under the workspace. <br>
Mitigation: Before use, disable transcript logging, log only metadata, redact sensitive content, or add retention cleanup according to the deployment's data handling requirements. <br>
Risk: Webhook requests can trigger a Moltbot agent when authenticated and a wake word is present. <br>
Mitigation: Use a strong webhook token, prefer Authorization headers where possible, and restrict the authority of the Fieldy agent that receives webhook-triggered messages. <br>


## Reference(s): <br>
- [Moltbot Webhooks Documentation](https://docs.molt.bot/automation/webhook.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/mrzilvis/skills/fieldy-ai-webhook) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, code, shell commands] <br>
**Output Format:** [Markdown with JSON and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes webhook configuration guidance and a JavaScript transform that can trigger an agent or append transcript entries to local JSONL files.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata and release changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
