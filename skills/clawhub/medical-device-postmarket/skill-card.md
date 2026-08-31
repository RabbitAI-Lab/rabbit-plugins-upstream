## Description:

A hands-on medical device post-market surveillance playbook for comparing US, EU, China, and Japan obligations, checking adverse event reporting timelines, and generating PMS, PSUR, FSCA/recall, and PMCF working frameworks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Regulatory affairs, quality, and clinical leaders use this skill to structure post-market surveillance work after medical device approval, including obligation comparison, report timing checks, PMS plans, PSUR outlines, and recall or FSCA process planning. Agent users can also run the local toolkit to produce structured command-line outputs and Markdown document skeletons.

### Deployment Geography for Use:

Global, with regulatory content focused on the United States, European Union, China, and Japan.

## Known Risks and Mitigations:

Risk: The bundled SECURITY_AUDIT.md contains copied references to a different package, weakening confidence in the artifact's own safety assurances.

Mitigation: Treat the included audit as unreliable for this release until the publisher regenerates it for the exact package and review the server security verdict before installation.

Risk: Medical device regulatory obligations and reporting timelines can change after publication.

Mitigation: Verify all jurisdiction-specific guidance against current official FDA, European Commission, SAMR, NMPA, PMDA, or other applicable regulator sources before relying on it.

## Reference(s):

- [上市后监管知识库（专题实操版）](references/上市后监管知识库.md)
- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/medical-device-postmarket)
- [FDA Medical Device Reporting](https://www.fda.gov/medical-device-reporting-mdr)
- [eCFR 21 CFR Part 803](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803)
- [European Commission MDCG 2022-21 PSUR guidance](https://health.ec.europa.eu/document/download/a7df24c3-d4a3-4218-a8e0-726febfa01c2_en?filename=mdcg_2022-21_en.pdf)
- [European Commission MDCG endorsed guidance](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en)
- [SAMR medical device adverse event monitoring measures](https://www.samr.gov.cn/cms_files/filemanager/samr/www/samrnew/samrgkml/nsjg/bgt/202106/W020211127427208653527.pdf)
- [China medical device adverse event monitoring system](http://maers.adrs.org.cn/)
- [PMDA medical device adverse event reporting](https://www.pmda.go.jp/safety/reports/mah/0006.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional local CLI commands and generated Markdown outlines]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled Python toolkit is described as zero-dependency and local, emitting results to standard output.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact frontmatter and manifest state 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
