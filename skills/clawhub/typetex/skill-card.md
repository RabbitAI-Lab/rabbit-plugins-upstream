## Description: <br>
Compile Typst and LaTeX documents to PDF through the TypeTex API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gregm711](https://clawhub.ai/user/gregm711) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to send Typst or LaTeX source and supporting files to TypeTex and receive PDF output. It supports single-file and multi-file document compilation with error details for troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Typst or LaTeX source, auxiliary files, images, fonts, bibliographies, and compiler logs may be sent to the external TypeTex API. <br>
Mitigation: Use public or low-sensitivity documents only unless there is approval to share confidential, proprietary, regulated, client, or secret-bearing material with TypeTex. <br>
Risk: Compilation logs and error messages may expose document details during troubleshooting. <br>
Mitigation: Treat logs as potentially sensitive and avoid sharing them outside approved channels. <br>


## Reference(s): <br>
- [TypeTex Public Compile API OpenAPI spec](artifact/openapi.yaml) <br>
- [Typst Documentation](https://typst.app/docs/) <br>
- [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX) <br>
- [TypeTex](https://typetex.app) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with JSON API payloads, Python examples, curl commands, and base64-encoded PDF responses from TypeTex.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [API responses include success status, pdf_base64 on success, error details, and LaTeX log output on some failures.] <br>

## Skill Version(s): <br>
1.5.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
