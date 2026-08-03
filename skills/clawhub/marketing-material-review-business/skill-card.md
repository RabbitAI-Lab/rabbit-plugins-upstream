## Description: <br>
Reviews marketing material from an advertising compliance perspective, including image review, risk annotation, and suggested revisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mabihuan](https://clawhub.ai/user/mabihuan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Brand, marketing, and compliance reviewers use this skill to screen Chinese marketing images, product pages, posters, livestream copy, and packaging for advertising and labeling risks. It produces OCR-based findings, annotated images, JSON risk files, and Markdown review reports for legal or business follow-up. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Marketing images may be sent to Baidu OCR or a configured OCR endpoint during automatic review. <br>
Mitigation: Use only approved images for OCR processing, keep BAIDU_OCR_ENDPOINT unset unless the destination is trusted, and reuse cached OCR JSON when repeat processing is needed. <br>
Risk: The launcher can load local dotenv files and expose unrelated credentials to the skill process. <br>
Mitigation: Run the skill from a clean working directory and use dedicated BAIDU_API_KEY and BAIDU_SECRET_KEY credentials scoped to OCR use. <br>
Risk: The skill can create a Python virtual environment and install dependencies at runtime. <br>
Mitigation: For production use, provide a pinned and preinstalled environment, or review requirements.txt before allowing automatic installation. <br>
Risk: Compliance findings are rule- and OCR-assisted and may miss context-specific legal requirements. <br>
Mitigation: Treat outputs as screening material and have qualified legal or compliance reviewers verify launch decisions against product attributes, substantiation, and current regulations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mabihuan/skills/marketing-material-review-business) <br>
- [Baidu AI OCR](https://ai.baidu.com) <br>
- [Compliance rules](references/compliance-rules.md) <br>
- [Risk rules](references/risk-rules.json) <br>
- [Forbidden words](references/forbidden-words.md) <br>
- [Common cases](references/common-cases.md) <br>
- [Advertising law](references/advertising-law.md) <br>
- [GB 7718-2025 food labeling](references/gb-7718-2025-food-labeling.md) <br>
- [GB 28050-2025 nutrition labeling](references/gb-28050-2025-nutrition-labeling.md) <br>
- [Barcode compliance rules](references/barcode-compliance-rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, code, shell commands, guidance] <br>
**Output Format:** [Markdown reports, JSON risk files, annotated image files, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create OCR JSON, rule risk JSON, agent payload and prompt files, final risk JSON, key-risk JSON, annotated PNG images, and review Markdown.] <br>

## Skill Version(s): <br>
1.1.10 (source: server release evidence and SKILL.md version notes) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
