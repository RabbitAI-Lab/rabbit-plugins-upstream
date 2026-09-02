## Description:

SaMD（Software as a Medical Device）软件即医疗器械专题技能，帮助判断 SaMD/嵌入式软件边界，并围绕 IMDRF N12 风险分类、IEC 62304 软件生命周期、FDA 软件关注等级、EU MDR 规则 11、网络安全与 SBOM 组织合规清单和官方参考入口。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Regulatory, quality, product, and engineering teams use this skill to structure SaMD classification, software lifecycle, cybersecurity, human factors, and submission-document planning. It is a regulatory reference aid and does not replace official classification decisions, legal advice, or qualified regulatory review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat regulatory reference output as legal advice or a final regulator classification.

Mitigation: Use the skill as a planning aid and route product-specific conclusions through qualified regulatory, legal, or official review.

Risk: Medical-device software guidance can change by jurisdiction and publication date.

Mitigation: Confirm current requirements through the linked official sources before applying guidance to submissions or product decisions.

Risk: The bundled audit helper writes a local security_results.json file when intentionally run.

Mitigation: Run the helper only in a reviewed local copy of the skill directory and inspect generated files before publishing or committing them.

## Reference(s):

- [SaMD知识库.md](references/SaMD知识库.md)
- [IMDRF Documents](https://www.imdrf.org/documents)
- [MDCG Guidance Documents](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en)
- [European Commission Medical Devices Sector](https://health.ec.europa.eu/medical-devices-sector)
- [FDA Guidance Document Search](https://www.fda.gov/regulatory-information/search-fda-guidance-documents)
- [FDA Device Advice](https://www.fda.gov/medical-devices/device-advice-comprehensive-regulatory-assistance)
- [CMDE](https://www.cmde.org.cn/)
- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/medical-device-samd)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown guidance with tables, checklists, and official reference links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be reviewed against current official regulatory sources before use in product or submission decisions.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
