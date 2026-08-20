## Description:

Sites to IMA crawls a target website's content list, exports xlsx/csv indexes, creates IMA category-index notes, imports selected URLs into an IMA knowledge base, and generates an incremental update manual.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sedey999](https://clawhub.ai/user/sedey999)

### License/Terms of Use:

MIT-0

## Use Case:

IMA Copilot users use this skill to turn professional media or blog websites into structured IMA knowledge-base content with category index notes, URL imports, exported tables, and repeatable incremental updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can crawl websites, append IMA notes, import URL batches into a knowledge base, and persist local progress, so a mistaken target can create durable records.

Mitigation: Require explicit target knowledge base, folder, and notebook details, then review the execution plan and import counts before any import.

Risk: The skill includes package-manager recovery guidance that can kill processes and remove dpkg lock files.

Mitigation: Treat the dpkg lock-removal command as manual troubleshooting only and do not allow an agent to run it automatically.

Risk: Broad update phrases can modify the wrong site's notes or knowledge-base records.

Mitigation: Use explicit update requests naming the exact site and target knowledge base, and require disambiguation when multiple progress records match.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sedey999/skills/sites-to-ima)
- [IMA Copilot](https://ima.qq.com)
- [Manual Template](references/manual-template.md)
- [Note Formats](references/note-formats.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown instructions and tables, JSON progress files, xlsx/csv exports, shell commands, and IMA API action guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or appends IMA notes, imports batches of URLs into a knowledge base, and stores local progress for incremental updates.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
