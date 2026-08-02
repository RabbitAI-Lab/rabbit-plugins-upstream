## Description: <br>
AI-powered pet sneeze/cough detection from real-time camera or uploaded pet media, with optional audio fusion, event frequency tracking, structured reports, and historical report lookup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, pet owners, boarding operators, and veterinary staff can use this skill to analyze pet video or media URLs for sneeze and cough events, frequency patterns, and non-diagnostic respiratory behavior observations. It can also retrieve cloud-hosted historical reports for the account-linked identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet videos, media URLs, and generated reports are processed by the publisher's cloud service. <br>
Mitigation: Use only media you are permitted to share and avoid sensitive home, clinic, or boarding-facility footage unless privacy and retention terms are acceptable. <br>
Risk: The skill may silently use or create an account-linked identity and store tokens locally. <br>
Mitigation: Run it in a controlled workspace, review local credential storage before and after use, and avoid shared machines for sensitive analyses. <br>
Risk: Detection results concern respiratory health behavior and can be mistaken for medical diagnosis. <br>
Mitigation: Treat outputs as behavioral observations only and refer frequent, severe, or ambiguous events to a qualified veterinarian. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-sneeze-cough-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Pet sneeze/cough API documentation](references/api_doc.md) <br>
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files, guidance] <br>
**Output Format:** [Markdown or JSON-style structured analysis text, with optional saved output file and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include event type, timing, frequency, risk prompts, suggestions, and cloud report URLs; historical lookup is returned as a Markdown table when available.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
