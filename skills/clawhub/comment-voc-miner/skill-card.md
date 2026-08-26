## Description:

Turn public comments into a usable brief. Give a post link, a category to search, or comments you already copied, and get the objections, verbatim lines, purchase worries, FAQ answers, live-commerce replies, and spoken hooks that come from what viewers actually wrote.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, ecommerce, social media, and customer research teams use this skill to turn public or pasted social comments into a same-day voice-of-customer brief. It supports objection mining, FAQ drafting, live-commerce replies, and spoken hooks based on audience wording.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports a broad shared Beatra authorization that exceeds the narrow comment-mining workflow.

Mitigation: Install only when that authorization is acceptable, keep credentials private, and revoke the device authorization from the Beatra console when the skill is no longer needed.

Risk: The security evidence reports an unrestricted bundled tool caller and local upload support.

Mitigation: Use only the documented comment lookup workflow and avoid generic upload or arbitrary tool-call paths unless that broader access is intended.

Risk: The security evidence reports silent automatic package updates by default.

Mitigation: Disable automatic updates with scripts/mcp_client.py update --auto off when manual review before updates is required.

## Reference(s):

- [Comment VOC Miner on ClawHub](https://clawhub.ai/beatra-ai/skills/comment-voc-miner)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)
- [Beatra skill homepage](https://beatra.ai/skills/comment-voc-miner)
- [Looking up comments](references/comment-lookup.md)
- [Writing the brief](references/brief.md)
- [Comment brief workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown brief with optional lookup status and billing fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are based on pasted comments or confirmed paid public comment lookups; no generated media artifact is expected.]

## Skill Version(s):

0.1.1 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
