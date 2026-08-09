## Description:

Blackstone Longform Fiction is a Chinese-language writing assistant for medium- and long-form fiction that helps authors develop ideas, outlines, characters, settings, style, chapters, revisions, and continuity checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jony4](https://clawhub.ai/user/jony4)

### License/Terms of Use:

MIT-0

## Use Case:

External fiction authors use this skill to turn ideas, outlines, character notes, or existing manuscript text into usable long-form fiction deliverables. It supports drafting, revision, local manuscript file handling, optional cloud story memory, and continuity checks across longer works.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can connect to Blackstone cloud services and save confirmed manuscript material and derived story data there by default once connected.

Mitigation: Install and enable cloud memory only when that storage behavior is acceptable; use local-only mode when manuscript material should not be sent to the cloud.

Risk: The skill can write local client configuration for the cloud service and open authorization or payment pages.

Mitigation: Authorize only through the publisher's Blackstone domain, keep credentials out of chat, and require the user to complete login and payment steps personally.

Risk: The security guidance flags silent self-updates of installed files.

Mitigation: Prefer a reviewed version or operational policy that requires explicit approval before skill updates in controlled environments.

Risk: Local manuscript file operations can change user-authored text if target files or requested edits are misunderstood.

Mitigation: Confirm target files and requested edit scope before writing, then reread or otherwise verify changed content after the write.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jony4/skills/blackstone-longform-fiction)
- [Server-Resolved GitHub Provenance](https://github.com/jony4/blackstone/tree/master/blackstone-longform-fiction)
- [Blackstone Website](https://blackstone.wansu.tech)
- [Quickstart Reference](references/quickstart.md)
- [Account and Authorization Reference](references/account.md)
- [Cloud Memory and MCP Workflow Reference](references/mcp.md)
- [Local File Management Reference](references/local-files.md)
- [Pricing Reference](references/pricing.md)
- [Troubleshooting Reference](references/troubleshooting.md)
- [Version and Updates Reference](references/updates.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown prose, manuscript text, diagnostic notes, and occasional shell commands or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update local manuscript files and, when connected, save confirmed manuscript material and derived story data to Blackstone cloud memory.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
