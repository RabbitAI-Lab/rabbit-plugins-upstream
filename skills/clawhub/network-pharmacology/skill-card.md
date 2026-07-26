## Description: <br>
Build evidence-graded compound-target-disease network-pharmacology hypotheses for natural products, herbal medicines, formulae, and small molecules using live SciMiner tools plus public life-science evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sciminer](https://clawhub.ai/user/sciminer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and life-science analysts use this skill to curate compounds, grade compound-target-disease evidence, route SciMiner analyses, and produce reproducible network-pharmacology reports. It supports hypothesis generation and evidence handoff, not claims of mechanism, efficacy, causality, synergy, or clinical benefit. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated HTML reports may execute crafted input data in a browser because the security scan found an unsafe rendering pattern. <br>
Mitigation: Open generated HTML only from trusted input data or patch the renderer to avoid innerHTML for table-derived metrics before using untrusted inputs. <br>
Risk: The skill calls SciMiner services and may upload user-provided analysis inputs. <br>
Mitigation: Use it only for projects where SciMiner calls and input uploads are acceptable, and review data sensitivity before execution. <br>
Risk: SCIMINER_API_KEY is required for tool calls. <br>
Mitigation: Keep the key out of project files and outputs; rely on gateway injection and stop execution if the credential is unavailable. <br>


## Reference(s): <br>
- [Evidence model](references/evidence-model.md) <br>
- [SciMiner routing](references/sciminer-tool-routing.md) <br>
- [SciMiner tool API files](https://sciminer.tech/tool_api_files/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with CSV, JSON, and HTML report artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Expected artifacts include project_manifest.json, component_evidence.csv, target_evidence.csv, nodes.csv, edges.csv, network.json, network_report.html, and a concise narrative.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
