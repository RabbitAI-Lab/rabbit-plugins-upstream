## Description:

Forge defines a forge-agnostic git-host driver contract and helper for normalized PR/MR, issue, merge, visibility, auth, reference, and capability workflows across GitHub, GitLab, and Gitea.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to design, reason about, and call forge-portable workflows without hardcoding a single git host. It is most useful for agent pipelines that need normalized PR/MR, issue, merge, visibility, auth, reference-format, and capability behavior across GitHub, GitLab, and Gitea.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can perform real PR/MR creation, issue edits, and merge actions through authenticated forge CLIs.

Mitigation: Use it only in repositories where that level of forge access is intended, prefer dry-run review before live calls, and restrict available credentials to the intended forge and repository scope.

Risk: Ambiguous forge detection falls back to GitHub for backward compatibility.

Mitigation: Pass an explicit forge selection such as --forge=gitlab or --forge=gitea when the remote host is self-hosted or otherwise ambiguous.

Risk: Some Gitea and adapter implementation surfaces are documented as boundary or Phase 2 behavior rather than complete live adapters.

Mitigation: Check the capability matrix and driver return values before relying on native behavior, and use documented degrade paths when a capability is unavailable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/forge)
- [Driver Interface](driver-interface.md)
- [Capability Matrix](capability-matrix.md)
- [Dispatch](dispatch.md)
- [Adapters](adapters.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown documentation with shell command examples and Bash helper functions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper can emit dry-run command strings or execute authenticated forge CLI calls when sourced and invoked.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
