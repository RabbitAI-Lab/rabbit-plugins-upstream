## Description:

元习 is a cross-agent learning-loop skill that captures mistakes, corrections, insights, missing capabilities, stale knowledge, and external-interface failures as reusable .learnings/ entries for later sessions and skill improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to preserve project-local lessons from command failures, user corrections, missing capabilities, and better practices, then review, promote, or extract those lessons into reusable agent guidance or skill skeletons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Learning entries may become persistent agent guidance after promotion.

Mitigation: Review and scan entries before running promote, and avoid promoting private, sensitive, or unverified content.

Risk: Optional Claude and Codex hook templates can run review behavior broadly if installed without narrowing matchers.

Mitigation: Enable hooks only when that workflow is desired, scope matchers to the intended workspace, and remove the hook configuration when no longer needed.

Risk: Unpinned npm installs may fetch a newer package than the release under review.

Mitigation: Use pinned package versions for reproducible installation and release validation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-learn)
- [Project homepage](https://github.com/YottaMeta/yotta-learn)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-learn)
- [Examples](references/examples.md)
- [FAQ](references/faq.md)
- [Hook setup](references/hooks-setup.md)
- [Walkthroughs](references/walkthroughs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown entries and summaries, shell commands, configuration snippets, and generated skill skeleton files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local .learnings/ files and can optionally promote reviewed entries into AGENTS.md or CLAUDE.md.]

## Skill Version(s):

0.2.1 (source: SKILL.md frontmatter, package.json, CHANGELOG, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
