## Description:

Turns a company's official earnings script into a labeled plan and one narrated audio clip per section.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Companies and their production teams use this skill to turn approved earnings remarks into a labeled set of 8 to 20 spoken clips for investor updates, without adding unsupported financial claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Beatra client uses a shared full-scope device credential, allowing access beyond earnings narration.

Mitigation: Install only if full-scope Beatra access is acceptable; protect the local credential and avoid deployments requiring speech-only access.

Risk: The client can silently update its package files without separate approval.

Mitigation: Disable automatic updates and review new package versions before applying them when change control is required.

Risk: Paid voice cloning and speech generation may incur credits or misstate financial figures if inputs are wrong.

Mitigation: Require voice rights and explicit approval of live costs; check every spoken line against the official script and pronunciation table.

## Reference(s):

- [Earnings Script Reads on ClawHub](https://clawhub.ai/beatra-ai/skills/earnings-script-read)
- [Beatra skill homepage](https://beatra.ai/skills/earnings-script-read)
- [Earnings script voice workflow](artifact/references/workflow.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Audio]

**Output Format:** [Labeled text plan and MP3 audio clips]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One clip per labeled section; 8 to 20 clips, with 10 by default.]

## Skill Version(s):

0.1.9 (source: ClawHub release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
