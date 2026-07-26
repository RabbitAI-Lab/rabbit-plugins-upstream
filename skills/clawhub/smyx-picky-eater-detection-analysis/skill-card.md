## Description: <br>
Analyzes pet feeding-area videos or video URLs through server-side APIs to identify selective eating behaviors, summarize behavior frequency, and provide feeding-adjustment suggestions without diagnosing disease. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, pet-care operators, and developers can use this skill to analyze pet feeding-bowl videos for picky-eating behaviors such as sorting food, pushing kibble away, or sniffing and leaving, then review structured feeding-behavior reports and related suggestions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet-feeding videos or supplied video URLs are sent to Lifeemergence backend APIs with identity-linked report history. <br>
Mitigation: Use the skill only when the publisher's privacy and retention terms are acceptable, and avoid sensitive home, clinic, or boarding-facility footage unless processing is approved. <br>
Risk: The skill can silently create or reuse an identity and stores backend tokens in a local workspace SQLite database. <br>
Mitigation: Run it in an isolated workspace, restrict filesystem access, and clear local state or tokens before reusing the workspace for another user. <br>
Risk: The skill's security verdict is suspicious because it combines video upload, identity handling, cloud report lookup, and local token storage. <br>
Mitigation: Review the skill before installation and limit execution to environments where outbound API calls and local credential storage are acceptable. <br>


## Reference(s): <br>
- [Pet Picky Eater Detection API Documentation](artifact/references/api_doc.md) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-picky-eater-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON-like structured analysis text with report links, plus optional shell commands for running the skill] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save output to a file when the output path argument is used.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
