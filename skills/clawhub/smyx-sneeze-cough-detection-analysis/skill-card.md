## Description:

Analyzes pet activity video, with optional audio, to identify sneeze and cough events, summarize timing and frequency, and provide behavior-observation guidance without making a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, animal hospital staff, and boarding center operators use this skill to submit pet activity videos or URLs for sneeze and cough behavior analysis and to review historical detection reports. Results are intended for observation and triage support, not veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media and identity-bearing requests are sent to an external analysis service.

Mitigation: Use only videos that are appropriate to share with that service and review endpoint configuration before execution.

Risk: The skill may silently create or reuse a local identity and persist service tokens in the workspace database.

Mitigation: Run in a trusted workspace, avoid shared machines for sensitive use, and clear stored credentials when they are no longer needed.

Risk: Development or private endpoint configuration may be present.

Mitigation: Check and replace endpoint settings before installation or production use.

Risk: Behavior analysis may be mistaken for veterinary diagnosis.

Mitigation: Treat outputs as observation support only and consult a veterinarian for frequent, severe, or concerning symptoms.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-sneeze-cough-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Pet Sneeze/Cough Detection API Documentation](references/api_doc.md)
- [Common Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with event summaries, frequency observations, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can print results to stdout, write a requested output file, or return a Markdown table of historical reports.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
