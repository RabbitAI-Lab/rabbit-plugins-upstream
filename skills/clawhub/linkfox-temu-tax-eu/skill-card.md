## Description: <br>
Provides agent guidance and scripts for Temu Europe tax workflows through LinkFox, including tax report export, Galerie signatures, invoice queries and downloads, merchant report downloads, and merchant invoice uploads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and marketplace operators use this skill to call and troubleshoot Temu Europe tax and invoice APIs through LinkFox. It helps agents prepare API requests, manage required credentials, run helper scripts, and inspect saved JSON results. <br>

### Deployment Geography for Use: <br>
Europe for Temu EU tax workflows; globally usable by authorized agent environments. <br>

## Known Risks and Mitigations: <br>
Risk: The security scan says this skill requires LinkFox gateway credentials, Temu seller access tokens, and local disk storage for tax and invoice responses. <br>
Mitigation: Pass credentials only when needed, restrict access to the working directory and token store, and delete saved response files and saved Temu tokens when they are no longer required. <br>
Risk: The security scan notes that the artifact includes broader Temu API and credential utilities than the tax-only description suggests. <br>
Mitigation: Prefer the tax-specific scripts for normal use, and use the generic proxy or non-EU examples only when the broader Temu access is intentional and authorized. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-tax-eu) <br>
- [API Reference](references/api.md) <br>
- [Temu Access Token Guide](references/access-token.md) <br>
- [Authorization Flow](references/authorization-flow.md) <br>
- [Partner EU Tax Catalog](references/partner-eu-catalog.md) <br>
- [Tax API Documentation Index](references/apis/README.md) <br>
- [Temu Partner EU Tax Documentation](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896&sub_menu_code=6494bb7afd8048d380a13e92f6275d17) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to local files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Large API responses are summarized in stdout while full JSON responses are saved under the working directory.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
