## Description:

Turns a public-education legal topic into a labeled digital-human still, a speakable explainer script, and a talking clip for firm marketing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Lawyers and firm marketing teams create short, labeled digital-presenter clips that explain general legal topics to the public without addressing individual cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared Beatra bearer credential can grant broad access if exposed.

Mitigation: Keep the device credential private and revoke the connection if it is compromised.

Risk: Prompts and supplied files needed for media generation are sent to Beatra.

Mitigation: Avoid submitting confidential client or case material; use only approved public-education facts and look references.

Risk: The bundled client silently updates local package files by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if changes must be reviewed first.

Risk: A legal explainer may misstate legal facts or appear to depict a real lawyer.

Mitigation: Have the firm review the script and final clip, and retain the visible non-lawyer presenter label.

## Reference(s):

- [ClawHub release](https://clawhub.ai/beatra-ai/skills/legal-explainer-clip)
- [Publisher skill homepage](https://beatra.ai/skills/legal-explainer-clip)
- [Legal explainer workflow](references/workflow.md)
- [Installation and authorization](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Media files]

**Output Format:** [Still plan and narration script, followed by generated image, audio, and video files after approval]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The digital presenter must be visibly labeled as a non-lawyer; paid media steps require separate approval.]

## Skill Version(s):

0.1.7 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
