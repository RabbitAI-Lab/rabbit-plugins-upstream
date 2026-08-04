## Description: <br>
KingDoc helps an agent create, edit, convert, search, share, recover, and compliance-check Kingsoft Docs documents with local generation and OCR options. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and document users use KingDoc to let an agent manage Kingsoft Docs and WPS workflows, including document creation, uploads, conversion, permissions, version recovery, OCR, conflict handling, and compliance checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad read/write authority over Kingsoft personal and team documents can expose or alter sensitive content. <br>
Mitigation: Install only when that authority is acceptable, authorize the narrowest OAuth scopes available, and review actions that affect documents or permissions. <br>
Risk: Configuration secrets may be exposed if config.json is stored in shared or synced locations. <br>
Mitigation: Keep config.json out of shared folders and rotate the App Secret immediately if it is exposed. <br>
Risk: Permanent deletion, rollback, permission changes, uploads, shares, webhooks, and notifications can have lasting effects. <br>
Mitigation: Require manual confirmation before those actions and inspect the affected files, users, URLs, and target operations. <br>
Risk: OCR of sensitive images may leave the local environment if cloud OCR fallback is used. <br>
Mitigation: Use local Tesseract for sensitive images or confirm that cloud OCR is acceptable before processing them. <br>
Risk: Downloads and generated files may be written outside an intended workspace. <br>
Mitigation: Keep downloaded and generated outputs inside a dedicated output directory with appropriate access controls. <br>


## Reference(s): <br>
- [ClawHub kingdoc Release Page](https://clawhub.ai/fyniujin/skills/kingdoc) <br>
- [Kingsoft Open Platform](https://developer.kdocs.cn) <br>
- [WPS Open Platform](https://open.wps.cn) <br>
- [KingDoc Security Design](references/security.md) <br>
- [KingDoc Rate Limit and Hardware Strategy](references/rate_limit.md) <br>
- [KingDoc Workflow Reference](references/workflows.md) <br>
- [KingDoc Authentication Reference](references/auth.md) <br>
- [KingDoc Office Conversion Reference](references/office_references.md) <br>
- [KingDoc Error Codes](references/error_codes.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with command snippets, configuration guidance, API-style parameters, and generated document or analysis artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or modify local generated files and may call Kingsoft Docs APIs when configured with user-authorized credentials.] <br>

## Skill Version(s): <br>
3.4.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
