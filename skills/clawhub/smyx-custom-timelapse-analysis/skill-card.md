## Description:

Generates condensed album highlights from long videos by extracting segments that match user-specified keywords or target subjects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn local or URL-based video footage into custom time-lapse highlight summaries focused on selected people, pets, scenes, or events. It can also return account-linked history reports for prior analyses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media uploads and account-linked history queries can expose personal video content or prior report history.

Mitigation: Disclose these actions to the user and confirm consent before sending media or querying historical reports.

Risk: Automatic account handling and local token persistence may create or retain identity-linked credentials without clear user awareness.

Mitigation: Avoid silent identity creation where possible and store any tokens in a real secret store or avoid persisting them.

Risk: Development and test configuration files include HTTP endpoints.

Mitigation: Default installations should use HTTPS production endpoints and review or remove non-production endpoint configuration before deployment.

Risk: A dependency name may be incorrect.

Mitigation: Correct the dependency specification before installation and verify dependency resolution in a clean environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-custom-timelapse-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text and JSON-like structured analysis with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include exported report links and historical report records.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; artifact SKILL.md frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
