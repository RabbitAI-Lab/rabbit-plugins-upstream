## Description:

Creates a set of 4 to 8 hall FAQ materials stills from public Xiaohongshu complaints and confirmed document facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Hall and public-service teams use the skill to turn public Xiaohongshu FAQ complaints and verified document requirements into one materials still per complaint. It can plan from pasted complaints when public note lookup is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device connection grants broad media, task, artifact, and wallet-related authority beyond this still-image workflow and stores a local bearer token.

Mitigation: Review the requested access before authorizing, protect the local credential, and revoke the device in Beatra Console when finished.

Risk: The package can silently install newer versions by default.

Mitigation: Review updates before use or disable automatic updates with `python3 scripts/mcp_client.py update --auto off`.

Risk: The client sends coarse installation and runtime registration data to Beatra.

Mitigation: Review the registration disclosure and use the skill only if this reporting is acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/xiaohongshu-hall-faq-stills)
- [Beatra skill homepage](https://beatra.ai/skills/xiaohongshu-hall-faq-stills)
- [Hall FAQ still workflow](artifact/references/workflow.md)
- [Hall FAQ lookup](artifact/references/hall-faq-lookup.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Images, Text, Markdown]

**Output Format:** [Image artifacts and a Markdown complaint-to-materials plan with task and billing details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically 4 to 8 stills; report actual image MIME type, dimensions, size, and net charged credits when available.]

## Skill Version(s):

0.1.8 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
