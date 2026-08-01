## Description: <br>
AI image generation and editing for agents across text-to-image and image-to-image workflows, video generation, audio generation, and image-to-3D asset creation through one zero-setup hosted runtime. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[danielgwilson](https://clawhub.ai/user/danielgwilson) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use Luxin to generate or edit creative media assets, including images, video, audio, and image-to-3D outputs, through a hosted CLI and HTTP API with durable media URLs and recoverable job records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and uploaded images are sent to a hosted external media service, and job, activity, and feedback records may be stored. <br>
Mitigation: Use Luxin only when hosted processing and storage are acceptable for the content being handled. <br>
Risk: Media creation and credit top-up flows can initiate payment-related actions when authorized. <br>
Mitigation: Start with guide or dry-run modes, set explicit spend caps, and require human or delegated-budget approval before credit purchases, Stripe Checkout, x402, or wallet settlement. <br>
Risk: Retrying a failed live media create without recovery checks could repeat paid provider work. <br>
Mitigation: Inspect recovery guidance, job status, activity records, or payment status before retrying live create or payment commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/danielgwilson/skills/luxin) <br>
- [Publisher profile](https://clawhub.ai/user/danielgwilson) <br>
- [Luxin homepage](https://luxin.sh) <br>
- [Canonical skill contract](https://luxin.sh/skill.md) <br>
- [Luxin LLM contract](https://luxin.sh/llms.txt) <br>
- [Luxin CLI contract](https://luxin.sh/cli.md) <br>
- [Hosted API](https://api.luxin.sh) <br>
- [Local CLI reference](references/cli.md) <br>
- [Local LLM reference](references/llms.txt) <br>
- [Local command contract](references/commands.json) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON response envelopes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Successful hosted generation or edit calls return durable media URLs, job IDs, asset IDs, trace IDs, cost receipts, and capability metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
