## Description: <br>
Reviews marketing images and layouts for advertising and food-label compliance, marks risk locations, and suggests concrete edits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mabihuan](https://clawhub.ai/user/mabihuan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Brand, marketing, and compliance teams use this skill to review packaging, e-commerce detail pages, banners, posters, live-stream copy, and other campaign assets for advertising and labeling risks. It can produce annotated images, risk reports, JSON payloads, and revision guidance for human review. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Reviewed images may be sent to Baidu OCR and OCR/report artifacts may be saved locally. <br>
Mitigation: Use the skill only with campaigns approved for remote OCR processing, choose a dedicated output directory, and remove local artifacts after handling confidential material. <br>
Risk: The launcher can load local credential/configuration files and auto-install Python dependencies. <br>
Mitigation: Run from a trusted working directory, avoid untrusted .env files, and pin or review dependencies before first use. <br>
Risk: OCR endpoint configuration can affect where image content is sent. <br>
Mitigation: Restrict OCR endpoint variables to Baidu hosts and verify environment settings during preflight checks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mabihuan/skills/marketing-material-review-business) <br>
- [Baidu AI OCR](https://ai.baidu.com) <br>
- [Advertising law reference](references/advertising-law.md) <br>
- [Compliance rules](references/compliance-rules.md) <br>
- [Common review cases](references/common-cases.md) <br>
- [Forbidden words](references/forbidden-words.md) <br>
- [Risk rules](references/risk-rules.json) <br>
- [GB 7718-2025 food labeling](references/gb-7718-2025-food-labeling.md) <br>
- [GB 28050-2025 nutrition labeling](references/gb-28050-2025-nutrition-labeling.md) <br>
- [Barcode compliance rules](references/barcode-compliance-rules.md) <br>
- [SC food production license rules](references/sc-food-production-license.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, annotated image files, JSON risk payloads, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save OCR results, agent-review prompts, risk JSON, and annotated output files in a local output directory.] <br>

## Skill Version(s): <br>
1.1.8 (source: server release evidence and SKILL.md version note, released 2026-08-01) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
