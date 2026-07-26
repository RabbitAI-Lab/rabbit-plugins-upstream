## Description: <br>
Writes, reviews, and fixes HTML markup for semantic structure, forms, accessibility, document head metadata, media, embeds, HTML email, parsing issues, internationalization, performance-sensitive markup, and untrusted HTML handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to author, review, and debug HTML markup across pages, forms, accessibility patterns, metadata, media embeds, email templates, and user-generated content. It is also used to maintain durable local notes about HTML decisions, audits, quirks, and reusable artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automatically reads and modifies persistent local memory under ~/Clawic/data/, including HTML notes, project records, domain records, audits, and artifacts. <br>
Mitigation: Install only when this long-lived local memory behavior is acceptable, and review the files it plans to update before relying on or sharing the stored notes. <br>
Risk: Pasted markup can contain API keys, verification tokens, signed URLs, session identifiers, or email service credentials. <br>
Mitigation: Strip secret values before writing memory and keep only pointers such as env:, keychain:, or password-manager locators. <br>
Risk: Guidance for untrusted HTML can affect XSS exposure if sanitization, escaping, or iframe sandboxing is applied incorrectly. <br>
Mitigation: Use maintained allowlist sanitizers, validate URL schemes, escape by output context, and document sanitizer allowlists when agreed. <br>


## Reference(s): <br>
- [ClawHub HTML skill page](https://clawhub.ai/ivangdavila/skills/html) <br>
- [Clawic HTML skill page](https://clawic.com/skills/html) <br>
- [Clawic skill library](https://clawic.com) <br>
- [Artifact: security guidance](artifact/security.md) <br>
- [Artifact: memory template](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown prose with HTML snippets and occasional configuration or file-update instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update local Clawic memory files when work produces durable findings; secrets are stripped before any memory write.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
