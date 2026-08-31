## Description:

Guides agents through CTF-focused web exploitation, reverse engineering, and source-code audit workflows covering HTTP vulnerabilities, JWT and injection analysis, Ghidra headless disassembly, and semgrep review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yxy050208](https://clawhub.ai/user/yxy050208)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security practitioners use this skill to triage authorized CTF web challenges, reverse engineering tasks, and source-code audit exercises. It helps plan reconnaissance, select exploitation or analysis techniques, and produce commands, code snippets, and concise findings for lab targets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes broad, actionable exploit and bypass playbooks that could be misapplied outside CTF or security-research settings.

Mitigation: Use it only on owned, lab, CTF, or explicitly authorized targets, and require human review before running generated commands.

Risk: Reverse-engineering and malware-like analysis workflows may interact with untrusted binaries or sensitive files.

Mitigation: Run analysis in isolated VMs or containers and avoid applying the workflows to real systems or sensitive binaries without authorization.

## Reference(s):

- [CTF Web & Reverse Audit Skill](SKILL.md)
- [CTF Web Exploitation Reference](references/ctf-web/SKILL.md)
- [CTF Reverse Engineering Reference](references/ctf-reverse/SKILL.md)
- [Security Arsenal Reference](references/security-arsenal/SKILL.md)
- [ClawHub Skill Page](https://clawhub.ai/yxy050208/skills/ctf-web-reverse-audit)
- [pycdc](https://github.com/zrax/pycdc)
- [pwndbg](https://github.com/pwndbg/pwndbg)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include offensive security commands and reverse-engineering workflows for authorized CTF or lab targets.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
