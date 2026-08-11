## Description:

Creates, refines, resumes, publishes, and queries polished PersonWise courses from topics, text, documents, or reference images through the PersonWise CLI with explicit approval for CLI install or update and browser OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

External course authors and agent operators use this skill to create, review, refine, publish, share, or query PersonWise courses from topics, supplied text, documents, and images while preserving source, access, and approval boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update the PersonWise CLI.

Mitigation: Require explicit approval and use only the bundled pinned bootstrap or exact CLI-provided update command.

Risk: Browser OAuth is required for PersonWise account access.

Mitigation: Use the browser or device flow and do not handle passwords, OTPs, tokens, authorization codes, cookies, or callback URLs.

Risk: Course creation can consume existing PersonWise course credits.

Mitigation: Run readiness before creation, stay within the authorized course count, and never purchase credits automatically.

Risk: Named documents or images may be uploaded to PersonWise.

Mitigation: Upload only user-named or explicitly approved files, require approval for agent-discovered local files, and avoid exposing signed URLs or private contents.

Risk: Link access can make a course accessible to anyone with the link.

Mitigation: Default to private access unless broader visibility is requested, and report the final access mode and matching URL from returned state.

## Reference(s):

- [Create a PersonWise Course](https://clawhub.ai/personwiseai/skills/personwise-create-course)
- [Connect and authorize the PersonWise CLI](references/connection-and-auth.md)
- [Design a high-quality PersonWise course](references/course-design.md)
- [Course classes, teaching archetypes, and editorial authority](references/course-archetypes.md)
- [PersonWise CLI workflow and recovery](references/workflow.md)
- [Capability-aware visual quality](references/visual-quality.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON command inputs, and secret-free completion records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports run and project IDs, source status, review evidence, final access mode, and playability state when available.]

## Skill Version(s):

2.1.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
