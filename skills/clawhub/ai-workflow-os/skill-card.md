## Description:

Routes complex AI-assisted work across project lifecycle guidance, formal governance, coding execution, session memory, web-research intake, and cross-source synthesis while keeping one owner per state surface.

This skill is ready for commercial/non-commercial use.

## Publisher:

[englandtong](https://clawhub.ai/user/englandtong)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to route multi-surface AI-assisted work among research, governance, implementation, memory, and synthesis workflows. It is useful when a request spans several specialist skills and needs explicit handoffs, authority boundaries, and evidence-backed next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A routing recommendation may influence which specialist skill handles writes, uploads, migrations, or destructive work.

Mitigation: Review the selected route before allowing writes, uploads, migrations, or destructive actions, and require explicit approval where the artifact calls for it.

Risk: Fallback modules could be mistaken for full specialist execution or independent acceptance.

Mitigation: Label fallback and unexecuted stages clearly, and avoid completion or acceptance claims unless the authorized specialist or role actually performed them.

Risk: External, uploaded, cloud, or sensitive materials may be routed into intake or archive workflows.

Mitigation: Treat such content as untrusted data, preserve provenance, and require confirmation before cloud upload or permanent archive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/englandtong/skills/ai-workflow-os)
- [Migration From The Monolithic v1 Design](references/migration-guide.md)
- [Platform Operation Guide](references/platform-operation-guide-zh.md)
- [Source Trust Levels](references/source-trust-levels.md)
- [Usage Examples](references/usage-examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bilingual English/Chinese guidance; no executable install payload.]

## Skill Version(s):

2.1.0 (source: server release evidence and artifact Version fields)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
