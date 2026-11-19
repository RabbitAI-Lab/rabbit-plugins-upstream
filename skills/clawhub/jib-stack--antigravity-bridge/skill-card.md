## Description:

Syncs configured Markdown files from Google Antigravity projects into an OpenClaw workspace for indexing and search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jib-stack](https://clawhub.ai/user/jib-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to sync selected Antigravity and Gemini project notes, rules, and documentation into an OpenClaw workspace so they can be indexed and searched.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured Markdown sources may contain confidential notes or credentials; the sync copies Markdown files without inspecting their contents.

Mitigation: Review configured source directories before syncing, and use --dry-run --verbose to inspect which files would be copied.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/jib-stack/skills/antigravity-bridge)
- [Mike Farah yq](https://github.com/mikefarah/yq)

## Skill Output:

**Output Type(s):** [Files, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Markdown files copied into the configured workspace, with YAML setup guidance and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Copies configured .md files into the selected OpenClaw workspace destination.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
