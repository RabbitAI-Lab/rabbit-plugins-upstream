## Description:

Finds relevant AI video workflows on varg how to and gives agents a matching tutorial, install options, and production steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use the skill to find a suitable workflow for a video request, compare options, and follow steps for planning and producing it. It helps with workflow discovery and instructions; video generation itself is handled by other tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries may contain confidential details and are logged by varg.

Mitigation: Keep confidential information out of search queries.

Risk: Recommended downstream skills may send media or project files to external services.

Mitigation: Review downstream skills and confirm what files leave your machine before installing or running them.

Risk: Remote pages and content may change after this release was reviewed.

Mitigation: Review fetched content before following its instructions; this security review covers the bundled instructions, not future remote content.

Risk: Optional account access, backups, or catalog publishing could affect personal or published data.

Mitigation: Use account access, backups, and publishing actions only when intended.

## Reference(s):

- [varg how to](https://varg.ai/how-to)
- [Whole video prompt](artifact/references/whole-video-prompt.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with workflow recommendations, install commands, and production steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides discovery and planning guidance; does not generate video itself.]

## Skill Version(s):

1.0.15 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
