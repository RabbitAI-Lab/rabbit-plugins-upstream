## Description: <br>
Skill Audit & Publish is an audit-first pipeline for publishing OpenClaw skills to ClawHub through sanitize, transform, verify, publish, and install-check stages with explicit approval before irreversible steps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to prepare OpenClaw skills for public ClawHub release by transforming content, auditing for personal data and credentials, collecting explicit approval, publishing, and install-checking the release. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publishing a skill publicly can expose incorrect slug, version, description, file set, or sanitization results if the verification message is not reviewed. <br>
Mitigation: Require explicit user approval of the slug, version, description, files, and sanitization status before running the publish command. <br>
Risk: Skill content may contain personal data, credentials, internal paths, or model-specific references before release. <br>
Mitigation: Run the sanitization checklist and have the user review any kept-with-reason items before publishing. <br>
Risk: The transform stage may add a Chinese summary to transformed descriptions that the publisher may not want. <br>
Mitigation: Review the full transformed description, including the Chinese summary, during the verification step. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/skill-audit-publish) <br>
- [Sanitization Checklist](artifact/sanitize.md) <br>
- [Transforming Content to Skill Format](artifact/transform.md) <br>
- [Pre-Publish Verification](artifact/verify.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated publish-folder files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user approval before publishing and install-checks the published skill.] <br>

## Skill Version(s): <br>
1.1.3 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
