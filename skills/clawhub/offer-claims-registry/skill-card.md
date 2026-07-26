## Description: <br>
Curates exact marketing claim wording, evidence, disclosures, terms, review dates, and live offers through an append-only claims event stream. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, compliance, and operations teams use this skill to register, update, expire, or query claims and offers while preserving evidence provenance, disclosures, terms, and review dates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can maintain a local record of marketing claims and offer terms. <br>
Mitigation: Install it only when local claims or offer records are desired, and review persisted entries as part of the publishing workflow. <br>
Risk: Owner/write capability can approve, expire, or withdraw official claim or offer records. <br>
Mitigation: Grant owner/write capability only when the user is ready for canonical decisions; otherwise keep items as proposals or unresolved evidence gaps. <br>
Risk: Missing exact claim or offer wording can lead to placeholder or unsupported records. <br>
Mitigation: Require one exact verbatim claim or offer statement before registering or projecting new entries, and return NEEDS_INPUT when it is absent. <br>


## Reference(s): <br>
- [Claims Projection Contract](references/claims-ledger-schema.md) <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/offer-claims-registry) <br>
- [Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and structured claim or offer records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return NEEDS_INPUT when an exact claim or offer statement is missing; canonical writes require explicit write permission and host capability.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
