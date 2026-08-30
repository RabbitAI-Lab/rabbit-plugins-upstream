## Description:

Publish Preflight Studio checks pre-publish social and ad copy for compliance, audience fit, and reach, returns cited replacements and corrected copy, and can render a cover from approved wording.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, creators, and brand or client copy reviewers use this skill before publishing social posts or ads to screen risky claims, test audience reaction, score reach, produce corrected copy, and optionally render a cover from approved wording.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a persistent shared Beatra device credential with broad media, wallet, artifact, and task access.

Mitigation: Install only if this access is acceptable, avoid uploading sensitive local files, and revoke the Beatra device authorization when the skill is no longer needed.

Risk: Automatic package updates are silently enabled by default.

Mitigation: Use the documented update command to disable automatic checks when review before update is required.

Risk: Cover rendering is paid work and failed recovery could duplicate a generation request if request identity is not preserved.

Mitigation: Confirm wording, route, canvas, and price before rendering; use one stable client_request_id and poll the recorded task rather than creating a replacement task.

Risk: Compliance and audience reads may be useful pre-publish signals but are not measured audience research or legal approval.

Mitigation: Review the cited findings and corrected copy before publishing, especially for regulated-category claims or client-approved language.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/publish-preflight-studio)
- [Beatra skill homepage](https://beatra.ai/skills/publish-preflight-studio)
- [Screening the copy](references/compliance-screen.md)
- [Reading it as the audience](references/audience-read.md)
- [Preflight workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with structured findings, pasteable corrected copy, command snippets, and returned task or artifact details when a cover is rendered.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include platform verdicts, change lists, reader-profile reactions, hook and share scores, task IDs, artifact links, dimensions, and net charged credits.]

## Skill Version(s):

0.1.3 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
