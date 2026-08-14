## Description:

KLYC-PMM helps AI agents persist, sync, distill, search, back up, and recover long-term text memories through local shell scripts and an authenticated HTTPS memory service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sylncn](https://clawhub.ai/user/sylncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent operators use this skill to initialize persistent memory, push and search text memories, run file-watching sync, perform memory distillation with a DeepSeek API key, and recover memories from a recovery URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent background syncing can send selected workspace files to the remote memory service.

Mitigation: Review and limit watch targets before enabling watch mode or the daemon, and enable background syncing only when the selected files are appropriate for remote memory storage.

Risk: Recovery URLs function as sensitive credentials and may appear in MEMORY.md or shell history.

Mitigation: Treat the recovery URL as a password, avoid committing MEMORY.md, store the URL in a trusted secret store, and clear shell history after recovery commands.

Risk: Memory distillation can send memory contents to DeepSeek when the required API key is configured.

Mitigation: Run distillation only after accepting that data flow, and configure the DeepSeek key deliberately for environments where that processing is allowed.

Risk: The skill integrates paid remote services and payment-link flows.

Mitigation: Confirm the expected service tier, payment path, and remote-service terms before using upgrade commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sylncn/skills/klyc-pmm)
- [Kunlun Yaochi Homepage](https://kunlunyaochi.com)
- [PMM Full Architecture](artifact/references/pmm-full-architecture.md)
- [Pay Skill Packaging Standard](artifact/references/pay-skill-spec.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated local configuration or memory files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local memory, identity, watch configuration, recovery result, and daemon-related files while communicating with configured HTTPS services.]

## Skill Version(s):

9.2.9 (source: frontmatter, skill manifest, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
