## Description:

Find human-made visual and audio references for AI image, video, music, or code-driven video projects, then organize candidates for a person to review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and agents preparing visual or audio work use this skill to find and assess real-world references before generating or building a piece. It organizes candidate references by creative job and gives a person the final selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Model judging or optional container setup may expose more local files or project secrets than needed.

Mitigation: Restrict judging to approved reference images and provide only service-specific credentials.

Risk: Images, judging criteria, and search terms are sent to external services.

Mitigation: Use approved material and avoid sending confidential images or sensitive project details.

Risk: Optional helpers and actual host containment have not been verified by the static review.

Mitigation: Review and pin optional helpers, and authorize production use separately.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/vargai/skills/find-references)
- [Source repository (metadata homepage; provenance unavailable)](https://github.com/vargHQ/skills/tree/main/find-references)

## Skill Output:

**Output Type(s):** [Markdown, HTML, JSON, Guidance, Shell commands]

**Output Format:** [Markdown notes and reference links, an HTML review board, and JSON search records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Organizes candidates by reference job; final choices are made by a person.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
