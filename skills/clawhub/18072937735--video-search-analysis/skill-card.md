## Description:

Searches local or remote videos for target objects or natural-language descriptions and returns structured video retrieval results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to submit video files or video URLs with search text, locate matching footage, and review structured results or historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says the skill sends video files, video URLs, search text, and report history to lifeemergence.com services.

Mitigation: Use only with media and descriptions approved for that cloud service; avoid sensitive surveillance, personal, or business media unless the service and account controls are approved.

Risk: The security review says the skill creates or reuses account-linked cloud identities and stores tokens locally.

Mitigation: Run it in a workspace with private data storage, review identity assignment and token storage before use, and clear local credentials when the workspace is shared.

Risk: The security verdict is suspicious because remote processing controls are weakly scoped.

Mitigation: Review the skill's expected domains, network access, and permissions before deployment, and restrict use to approved endpoints.

## Reference(s):

- [Video Search Analysis API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/video-search-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with inline shell commands and JSON-style report content.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud-hosted report links and saved output files when requested.]

## Skill Version(s):

1.0.99 (source: ClawHub release metadata; artifact SKILL.md frontmatter says 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
