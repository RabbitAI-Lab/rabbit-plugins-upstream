## Description: <br>
This skill lets an agent search SmartLib's Chinese and global literature indexes, review article metadata and source links, and retrieve authorized Chinese journal PDFs or open-access full text through supported channels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[j-levee](https://clawhub.ai/user/j-levee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External researchers, students, librarians, and other knowledge workers use this skill to find academic literature, inspect citation metadata, trace source database links, and request full-text downloads when available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates and uses an external SmartLib account and stores the user's email in local configuration. <br>
Mitigation: Ask for only the email needed for SmartLib registration and quota management, and keep local configuration private. <br>
Risk: The skill sends literature queries to SmartLib Gateway and related open-access services. <br>
Mitigation: Avoid submitting sensitive, confidential, or unpublished research details unless the user accepts those external service dependencies. <br>
Risk: The skill supports paid quota flows and may present payment QR codes or gateway-provided links. <br>
Mitigation: Verify the destination, plan, amount, and order details before paying or clicking links. <br>
Risk: Gateway-provided notices and links may be forwarded into the chat. <br>
Mitigation: Treat forwarded notices as external service messages and review links before acting on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/j-levee/skills/global-biblio-base) <br>
- [README.md](README.md) <br>
- [PIPELINE.md](PIPELINE.md) <br>
- [SmartLib account and billing reference](references/account.md) <br>
- [SmartLib website](https://www.vipslib.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown search results with article metadata, source links, quota notices, and optional PDF or full-text download outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on SmartLib account status, available quota, network access, and whether the requested document is authorized or open access.] <br>

## Skill Version(s): <br>
3.9.3 (source: SKILL.md frontmatter and server release metadata, released 2026-07-22) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
