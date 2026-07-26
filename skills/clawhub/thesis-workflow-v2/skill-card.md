## Description: <br>
Write, review, and export MBA and academic theses end-to-end as Word/DOCX through outline planning, node-by-node drafting, review loops, academic deep review, and formatted export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hehe973781230](https://clawhub.ai/user/hehe973781230) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Students, academic writers, and their supporting agents use this skill to plan, draft, review, revise, and export MBA or academic thesis documents. It is intended for OpenClaw workflows that need structured checkpoints, multi-tool research, automated guardrails, and Word output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Thesis topics or document content may be sent to external search or document-parsing services. <br>
Mitigation: Use only with material approved for those services, and disable or review MinerU, cloud parsing, and external search paths before processing confidential, embargoed, or company-sensitive work. <br>
Risk: The skill may read local OpenClaw session or provider configuration. <br>
Mitigation: Review credential-discovery behavior before installation and run with scoped credentials that are acceptable for the thesis workflow. <br>
Risk: Installation or runtime behavior can modify the local Python environment. <br>
Mitigation: Install in an isolated environment and review dependency installation steps before running the workflow. <br>
Risk: The workflow stores local configuration and state files for thesis projects. <br>
Mitigation: Run in a controlled workspace and avoid storing sensitive thesis, company, or credential data in shared directories. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/hehe973781230/skills/thesis-workflow-v2) <br>
- [Publisher Profile](https://clawhub.ai/user/hehe973781230) <br>
- [README](artifact/README.md) <br>
- [English README](artifact/README_EN.md) <br>
- [Loop Design](artifact/references/loop-design.md) <br>
- [Chapter Summary Design](artifact/references/chapter-summary-design.md) <br>
- [Content Hint Fallback](artifact/references/content-hint-fallback.md) <br>
- [DOCX Export Skill](artifact/thesis-docx-export/SKILL.md) <br>
- [DOCX Export Checklist](artifact/thesis-docx-export/references/checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, Python entry points, workflow state files, review reports, and DOCX export artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are organized around OpenClaw phases, human-in-the-loop checkpoints, local workflow state, and thesis document artifacts.] <br>

## Skill Version(s): <br>
2.1.2-beta.1 (source: server release metadata and SKILL.md metadata.clawdbot.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
