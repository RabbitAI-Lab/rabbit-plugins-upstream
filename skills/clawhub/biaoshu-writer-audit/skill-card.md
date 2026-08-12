## Description:

标书合规性审查 helps agents use the 百炼®标书 cloud service to interpret tender files, generate bid documents, and produce compliance review reports with risk levels, evidence, and revision suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bidding teams use this skill to review tender and bid documents for compliance risks, similarity issues, and missing manual checks. It can also support tender interpretation and bid document generation when the user provides local files and an App Key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain business, pricing, or personal data and are uploaded to the 百炼®标书 cloud service for processing.

Mitigation: Confirm user awareness and consent before upload, and use only the disclosed service domain from the evidence.

Risk: The App Key is an account credential that could expose the user's account if pasted into chat or embedded in shared links.

Mitigation: Keep the App Key in the local config file, never ask the user to paste it into chat, and avoid forwarding URLs that contain credential parameters.

Risk: Generated bid documents may consume account points, and cloud results are retained for a limited period.

Mitigation: Tell users about point usage before bid generation and remind them that cloud results are retained temporarily under their account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-audit)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [Usage guide](references/usage.md)
- [API contract reference](references/api.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [User-facing text plus generated HTML, Word, and DOCX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local user-provided files and may produce report/document files with absolute local paths.]

## Skill Version(s):

1.0.5 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
