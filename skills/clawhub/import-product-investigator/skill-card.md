## Description: <br>
Investigates imported-product supply chains using public registries, product photos, traceability codes, and evidence grading to flag credential, labeling, authenticity, and consumer-fraud risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pisces33](https://clawhub.ai/user/pisces33) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Consumers, analysts, and support agents use this skill to investigate whether an imported product appears properly registered, traceable, and supported by independent evidence before relying on it or escalating a complaint. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product photos, purchase receipts, screenshots, and payment-record images may be saved locally in the investigation evidence package. <br>
Mitigation: Redact personal and financial details before sharing documents, and delete the local evidence package when it is no longer needed. <br>
Risk: Traceability-platform claims and registry results can be self-reported, incomplete, or time-sensitive, which can lead to overconfident product-authenticity conclusions. <br>
Mitigation: Date the report, cite the source for each factual claim, prefer independent official or brand evidence, and downgrade conclusions when only seller-controlled sources are available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pisces33/skills/import-product-investigator) <br>
- [General Administration of Customs Cifer query](https://ciferquery.singlewindow.cn/) <br>
- [National Enterprise Credit Information Publicity System](https://www.gsxt.gov.cn/) <br>
- [National Medical Products Administration](https://www.nmpa.gov.cn/) <br>
- [SAMR special food information query](https://bjzx.samr.gov.cn/sscxquery/) <br>
- [China Quality Certification Centre CNCA portal](https://www.cnca.gov.cn/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown investigation reports, concise summaries, evidence checklists, and occasional shell or browser command guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create a local evidence package under ~/.qclaw/workspace with user-provided images, screenshots, purchase records, and payment-record images.] <br>

## Skill Version(s): <br>
1.1.5 (source: frontmatter and server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
