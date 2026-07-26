## Description: <br>
Personal Genomics analyzes raw consumer DNA files locally to produce genetic health, pharmacogenomics, ancestry, trait, and report outputs without sending data off the machine. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[wkyleg](https://clawhub.ai/user/wkyleg) <br>

### License/Terms of Use: <br>
MIT License <br>


## Use Case: <br>
Developers and AI agents use this skill to analyze raw DNA files from consumer genetics services and VCF sources, then summarize medically relevant, ancestry, trait, pharmacogenomic, and quality findings. Outputs are intended for informational screening and research-oriented interpretation, not diagnosis or treatment decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles extremely sensitive DNA-derived health, ancestry, carrier, medication, and family-related information and writes rich reports to local disk. <br>
Mitigation: Use a dedicated local output folder, avoid cloud-synced or shared directories, encrypt or delete reports when finished, and treat generated files as sensitive records. <br>
Risk: The skill can surface high-impact medical, cancer, carrier, pharmacogenomic, ancestry, and sex-related inferences without enough guardrails for clinical use. <br>
Mitigation: Treat results as informational screening only, confirm important findings with clinical-grade testing, and consult qualified healthcare professionals or genetic counselors before medical decisions. <br>


## Reference(s): <br>
- [Personal Genomics ClawHub Page](https://clawhub.ai/wkyleg/skills/personal-genomics) <br>
- [Genetic Results Interpretation Guide](references/INTERPRETATION_GUIDE.md) <br>
- [DNA Testing Privacy Guide](references/PRIVACY_GUIDE.md) <br>
- [CPIC Guidelines](https://cpicpgx.org/guidelines) <br>
- [PhyloTree](https://www.phylotree.org/) <br>
- [ISOGG Y-DNA Haplogroup Tree](https://isogg.org/tree/) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Text, HTML, PDF, Guidance] <br>
**Output Format:** [Local report files including agent_summary.json, full_analysis.json, report.txt, dashboard.html, genetic_report.pdf, and clinical export JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally and writes DNA-derived reports to disk; users should protect output folders because the reports can contain sensitive health, ancestry, medication, carrier, and family-related information.] <br>

## Skill Version(s): <br>
4.2.0 (source: release evidence and CHANGELOG, released 2026-02-07) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
